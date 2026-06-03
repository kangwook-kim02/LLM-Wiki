# raw/

인제스트할 원본 소스 파일을 보관하는 디렉토리입니다.

> **이 디렉토리의 파일은 `.gitignore`에 의해 Git 추적에서 제외됩니다.**
> 이 README.md 파일만 예외입니다.

---

## 저장 대상

| 파일 형식 | 예시 | 용도 |
|-----------|------|------|
| PDF | `langchain-docs.pdf`, `rag-survey.pdf` | 논문, 공식 문서, 튜토리얼 |
| 텍스트 | `notes.txt`, `summary.md` | 직접 작성한 메모, 요약본 |
| Markdown | `langraph-guide.md` | 외부에서 가져온 문서 |

## 파일 추가 방법

1. **Streamlit 뷰어** (정식 경로): 파일 업로드 패널에서 업로드 → `raw_save()` MCP 도구로 자동 저장
2. **개발/테스트용**: 이 디렉토리에 직접 파일 복사 후 `raw_read(filename)`으로 접근

## 주의사항

- 파일을 직접 수정하지 않는다 (`raw/` 파일은 불변 원본)
- 에이전트는 `raw_read(filename)` MCP 도구로만 읽는다 (내장 Read 도구 사용 금지)
- PDF 텍스트 추출은 인제스트 스킬이 처리한다 (이슈 #4)
