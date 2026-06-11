/**
 * chat.js — 채팅 패널 + AJAX 네비게이션
 *
 * - 채팅: POST /chat  {"message": "..."} → {"reply": "..."}
 * - 업로드: POST /upload  FormData → {"ok": true, "filename": "..."}
 * - 네비게이션: GET /api/page/<slug> → 본문만 교체 (채팅 패널 유지)
 */

(function () {
  "use strict";

  /* ===== AJAX 네비게이션 ===== */

  const mainContent = document.querySelector(".main-content");

  function setActiveNav(slug) {
    document.querySelectorAll(".nav-item").forEach(el => el.classList.remove("active"));
    const link = document.querySelector(`.nav-link[href="/page/${slug}"]`);
    if (link) link.closest(".nav-item").classList.add("active");
  }

  async function navigateTo(slug, pushState) {
    try {
      const res  = await fetch("/api/page/" + slug);
      const data = await res.json();

      if (mainContent) {
        mainContent.innerHTML = data.html;
        mainContent.scrollTop = 0;
      }

      document.title = data.title ? data.title + " — LLM Wiki" : "LLM Wiki";

      if (pushState) {
        history.pushState({ slug: slug }, document.title, "/page/" + slug);
      }

      setActiveNav(slug);
    } catch (err) {
      console.error("Navigation error:", err);
    }
  }

  // 사이드바 링크 클릭 인터셉트
  document.querySelectorAll(".nav-link").forEach(function (link) {
    link.addEventListener("click", function (e) {
      e.preventDefault();
      const slug = this.getAttribute("href").replace("/page/", "");
      navigateTo(slug, true);
    });
  });

  // 본문 내 내부 링크 인터셉트 (이벤트 위임 — AJAX 교체 후에도 동작)
  if (mainContent) {
    mainContent.addEventListener("click", function (e) {
      const link = e.target.closest("a");
      if (!link) return;
      const href = link.getAttribute("href");
      if (href && href.startsWith("/page/")) {
        e.preventDefault();
        const slug = href.replace("/page/", "");
        navigateTo(slug, true);
      }
    });
  }

  // 브라우저 뒤로가기 / 앞으로가기
  window.addEventListener("popstate", function (e) {
    if (e.state && e.state.slug) {
      navigateTo(e.state.slug, false);
    }
  });

  // 현재 페이지 slug를 초기 history state에 등록
  (function () {
    const active = document.querySelector(".nav-item.active .nav-link");
    if (active) {
      const slug = active.getAttribute("href").replace("/page/", "");
      history.replaceState({ slug: slug }, document.title, window.location.pathname);
    }
  })();

  /* ===== 키워드 검색 (V-05) ===== */

  const searchInput   = document.getElementById("search-input");
  const searchResults = document.getElementById("search-results");

  function renderSearchResults(items) {
    if (!searchResults) return;

    searchResults.innerHTML = "";

    if (items.length === 0) {
      const empty = document.createElement("div");
      empty.className = "search-no-results";
      empty.textContent = "검색 결과가 없습니다.";
      searchResults.appendChild(empty);
    } else {
      items.forEach(function (item) {
        const el = document.createElement("div");
        el.className = "search-result-item";
        el.setAttribute("tabindex", "0");
        el.setAttribute("role", "button");
        el.setAttribute("aria-label", item.title);

        const titleEl = document.createElement("div");
        titleEl.className = "search-result-title";
        titleEl.textContent = item.title;

        const excerptEl = document.createElement("div");
        excerptEl.className = "search-result-excerpt";
        excerptEl.textContent = item.excerpt || "";

        el.appendChild(titleEl);
        el.appendChild(excerptEl);

        function selectItem() {
          navigateTo(item.slug, true);
          searchInput.value = "";
          searchResults.hidden = true;
        }

        el.addEventListener("click", selectItem);
        el.addEventListener("keydown", function (e) {
          if (e.key === "Enter" || e.key === " ") {
            e.preventDefault();
            selectItem();
          }
        });

        searchResults.appendChild(el);
      });
    }

    searchResults.hidden = false;
  }

  let _searchTimer = null;

  if (searchInput) {
    searchInput.addEventListener("input", function () {
      const query = searchInput.value.trim();

      clearTimeout(_searchTimer);

      if (!query) {
        if (searchResults) searchResults.hidden = true;
        return;
      }

      _searchTimer = setTimeout(async function () {
        try {
          const res  = await fetch("/api/search?q=" + encodeURIComponent(query));
          const data = await res.json();
          renderSearchResults(data);
        } catch (err) {
          console.error("Search error:", err);
        }
      }, 300);
    });

    // 검색창 바깥 클릭 시 결과 숨김
    document.addEventListener("click", function (e) {
      if (searchResults && !searchInput.contains(e.target) && !searchResults.contains(e.target)) {
        searchResults.hidden = true;
      }
    });

    // Escape 키로 결과 닫기
    searchInput.addEventListener("keydown", function (e) {
      if (e.key === "Escape") {
        searchResults.hidden = true;
        searchInput.blur();
      }
    });
  }

  /* ===== 채팅 패널 ===== */

  const chatForm     = document.getElementById("chat-form");
  const chatInput    = document.getElementById("chat-input");
  const chatMessages = document.getElementById("chat-messages");
  const chatSpinner  = document.getElementById("chat-spinner");
  const sendBtn      = chatForm ? chatForm.querySelector(".chat-send-btn") : null;

  const fileInput    = document.getElementById("chat-file-input");
  const fileChip     = document.getElementById("chat-file-chip");
  const fileChipName = document.getElementById("chat-file-chip-name");
  const fileRemove   = document.getElementById("chat-file-remove");

  const tokenUsageEl = document.getElementById("chat-token-usage");

  /* ===== 세션 토큰 누적 ===== */

  const sessionTokens = { input: 0, output: 0 };

  function updateTokenDisplay() {
    if (!tokenUsageEl) return;
    tokenUsageEl.textContent =
      "입력 " + sessionTokens.input.toLocaleString() + " 토큰" +
      " · 출력 " + sessionTokens.output.toLocaleString() + " 토큰";
  }

  /* ===== 메시지 버블 ===== */

  function appendMessage(text, role) {
    const bubble = document.createElement("div");
    bubble.className = "chat-bubble " + role;
    bubble.textContent = text;
    chatMessages.appendChild(bubble);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  /* ===== 로딩 상태 (스피너 텍스트 사이클링 포함) ===== */

  const spinnerText = document.getElementById("chat-spinner-text");
  const _thinkingMessages   = ["Thinking...", "Almost there...", "Just a moment..."];
  const _thinkingThresholds = [0, 10000, 25000];
  let _thinkingTimer = null;

  function setLoading(on) {
    chatSpinner.classList.toggle("active", on);
    if (sendBtn)   sendBtn.disabled = on;
    if (chatInput) chatInput.disabled = on;
    if (fileInput) fileInput.disabled = on;

    if (on) {
      const start = Date.now();
      if (spinnerText) spinnerText.textContent = _thinkingMessages[0];
      _thinkingTimer = setInterval(function () {
        const elapsed = Date.now() - start;
        for (let i = _thinkingThresholds.length - 1; i >= 0; i--) {
          if (elapsed >= _thinkingThresholds[i]) {
            if (spinnerText) spinnerText.textContent = _thinkingMessages[i];
            break;
          }
        }
      }, 1000);
    } else {
      clearInterval(_thinkingTimer);
      if (spinnerText) spinnerText.textContent = "";
    }
  }

  /* ===== 파일 칩 관리 ===== */

  function showFileChip(name) {
    fileChipName.textContent = name;
    fileChip.hidden = false;
  }

  function clearFile() {
    if (fileInput)  fileInput.value = "";
    if (fileChip)   fileChip.hidden = true;
    if (fileChipName) fileChipName.textContent = "";
  }

  if (fileInput) {
    fileInput.addEventListener("change", function () {
      const file = fileInput.files[0];
      if (file) {
        showFileChip(file.name);
      } else {
        clearFile();
      }
    });
  }

  if (fileRemove) {
    fileRemove.addEventListener("click", function () {
      clearFile();
    });
  }

  /* ===== 파일 업로드 ===== */

  async function uploadFile(file) {
    appendMessage("📎 " + file.name + " 업로드 중…", "system");

    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("/upload", { method: "POST", body: formData });
    const data = await res.json().catch(() => ({}));

    if (res.ok && data.ok) {
      appendMessage("✅ " + data.filename + " 업로드 완료", "system");
      clearFile();
      return true;
    } else {
      appendMessage("❌ 업로드 실패: " + (data.error || "알 수 없는 오류"), "error");
      return false;
    }
  }

  /* ===== 채팅 전송 ===== */

  async function sendMessage(message) {
    appendMessage(message, "user");

    const res = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message }),
    });

    if (!res.ok) {
      const err = await res.json().catch(() => ({}));
      appendMessage(
        "오류: 서버 응답 " + res.status + (err.error ? " — " + err.error : ""),
        "error"
      );
      return;
    }

    const data = await res.json();
    if (data.usage) {
      sessionTokens.input  += data.usage.input  || 0;
      sessionTokens.output += data.usage.output || 0;
      updateTokenDisplay();
    }
    if (data.error) {
      appendMessage(data.reply || "알 수 없는 오류가 발생했습니다.", "error");
    } else {
      appendMessage(data.reply || "(응답 없음)", "assistant");
    }
  }

  /* ===== 폼 제출 ===== */

  if (chatForm) {
    chatForm.addEventListener("submit", async function (e) {
      e.preventDefault();

      const file    = fileInput && fileInput.files[0];
      const message = chatInput ? chatInput.value.trim() : "";

      if (!file && !message) return;

      setLoading(true);

      try {
        if (file) {
          const ok = await uploadFile(file);
          if (!ok) return;
        }

        if (message) {
          chatInput.value = "";
          await sendMessage(message);
        }
      } catch (err) {
        appendMessage("네트워크 오류: " + err.message, "error");
      } finally {
        setLoading(false);
        if (chatInput) chatInput.focus();
      }
    });

    if (chatInput) {
      chatInput.addEventListener("keydown", function (e) {
        if (e.key === "Enter" && !e.shiftKey) {
          e.preventDefault();
          chatForm.dispatchEvent(new Event("submit", { cancelable: true }));
        }
      });
    }
  }
})();
