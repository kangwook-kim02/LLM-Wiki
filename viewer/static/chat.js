/**
 * chat.js — 채팅 패널 + 파일 업로드 AJAX 핸들러 (V-03, V-04)
 *
 * - 채팅: POST /chat  {"message": "..."} → {"reply": "..."}
 * - 업로드: POST /upload  FormData → {"ok": true, "filename": "..."}
 */

(function () {
  "use strict";

  /* ===== 채팅 패널 ===== */

  const chatForm     = document.getElementById("chat-form");
  const chatInput    = document.getElementById("chat-input");
  const chatMessages = document.getElementById("chat-messages");
  const chatSpinner  = document.getElementById("chat-spinner");
  const sendBtn      = chatForm ? chatForm.querySelector(".chat-send-btn") : null;

  /**
   * 메시지 버블을 채팅 목록에 추가하고 최하단으로 스크롤한다.
   * @param {string} text
   * @param {"user"|"assistant"|"error"} role
   */
  function appendMessage(text, role) {
    const bubble = document.createElement("div");
    bubble.className = "chat-bubble " + role;
    bubble.textContent = text;
    chatMessages.appendChild(bubble);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  /** 전송 중 UI 잠금 */
  function setLoading(on) {
    chatSpinner.classList.toggle("active", on);
    if (sendBtn) sendBtn.disabled = on;
    if (chatInput) chatInput.disabled = on;
  }

  if (chatForm) {
    chatForm.addEventListener("submit", async function (e) {
      e.preventDefault();

      const message = chatInput.value.trim();
      if (!message) return;

      // 사용자 메시지 표시
      appendMessage(message, "user");
      chatInput.value = "";
      setLoading(true);

      try {
        const res = await fetch("/chat", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ message }),
        });

        if (!res.ok) {
          const err = await res.json().catch(() => ({}));
          appendMessage("오류: 서버 응답 " + res.status + (err.error ? " — " + err.error : ""), "error");
          return;
        }

        const data = await res.json();
        if (data.error) {
          appendMessage(data.reply || "알 수 없는 오류가 발생했습니다.", "error");
        } else {
          appendMessage(data.reply || "(응답 없음)", "assistant");
        }
      } catch (err) {
        appendMessage("네트워크 오류: " + err.message, "error");
      } finally {
        setLoading(false);
        chatInput.focus();
      }
    });

    // Shift+Enter: 줄바꿈, Enter 단독: 전송
    chatInput.addEventListener("keydown", function (e) {
      if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        chatForm.dispatchEvent(new Event("submit", { cancelable: true }));
      }
    });
  }

  /* ===== 파일 업로드 ===== */

  const uploadForm    = document.getElementById("upload-form");
  const uploadInput   = document.getElementById("upload-file-input");
  const uploadName    = document.getElementById("upload-file-name");
  const uploadResult  = document.getElementById("upload-result");
  const uploadBtn     = uploadForm ? uploadForm.querySelector(".upload-btn") : null;

  // 선택된 파일명 표시
  if (uploadInput) {
    uploadInput.addEventListener("change", function () {
      const file = uploadInput.files[0];
      uploadName.textContent = file ? file.name : "선택된 파일 없음";
      if (uploadResult) {
        uploadResult.textContent = "";
        uploadResult.className = "upload-result";
      }
    });
  }

  if (uploadForm) {
    uploadForm.addEventListener("submit", async function (e) {
      e.preventDefault();

      const file = uploadInput && uploadInput.files[0];
      if (!file) {
        setUploadResult("파일을 먼저 선택해 주세요.", false);
        return;
      }

      if (uploadBtn) uploadBtn.disabled = true;

      const formData = new FormData();
      formData.append("file", file);

      try {
        const res = await fetch("/upload", {
          method: "POST",
          body: formData,
        });

        const data = await res.json().catch(() => ({}));

        if (res.ok && data.ok) {
          setUploadResult("업로드 완료: " + data.filename, true);
          uploadInput.value = "";
          uploadName.textContent = "선택된 파일 없음";
        } else {
          setUploadResult("업로드 실패: " + (data.error || "알 수 없는 오류"), false);
        }
      } catch (err) {
        setUploadResult("네트워크 오류: " + err.message, false);
      } finally {
        if (uploadBtn) uploadBtn.disabled = false;
      }
    });
  }

  /**
   * 업로드 결과 메시지를 표시한다.
   * @param {string} msg
   * @param {boolean} success
   */
  function setUploadResult(msg, success) {
    if (!uploadResult) return;
    uploadResult.textContent = msg;
    uploadResult.className = "upload-result " + (success ? "success" : "error");
  }
})();
