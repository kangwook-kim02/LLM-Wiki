---
type: concept
tags: [non-parametric-memory, retrieval, knowledge-base, document-index]
created: 2026-06-03
sources: [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.pdf]
---

# Non-Parametric Memory (비파라미터 기억)

## 정의
모델 파라미터 외부에 명시적으로 저장된 지식으로, 검색(retrieval)을 통해 접근하는 외부 지식 베이스.

## 상세 설명
Non-parametric memory는 신경망 가중치가 아닌 외부 데이터 구조(예: 문서 인덱스, 데이터베이스)에 저장된 지식을 의미한다. 직접 수정·확장이 가능하고, 어떤 정보를 참조했는지 투명하게 추적할 수 있다는 장점이 있다.

[[concepts/rag]] 모델에서 non-parametric memory는 위키피디아 문서의 밀집 벡터 인덱스로 구현된다:
- 위키피디아 전체를 100단어 단위의 21M 청크로 분할
- 각 청크를 [[frameworks/dpr]] 문서 인코더(BERT-base)로 임베딩
- [[frameworks/faiss]] 기반 MIPS 인덱스로 저장
- 쿼리 인코더가 입력을 임베딩하면, [[concepts/mips]]로 top-K 문서를 검색

Non-parametric memory의 핵심 장점 중 하나는 **Index Hot-Swapping** ([[patterns/index-hot-swapping]])이다. 인덱스를 교체하면 모델 재학습 없이 세계 지식을 업데이트할 수 있다. 실험에서 2016년 인덱스와 2018년 인덱스를 교체했을 때, 각각의 세계 리더 정보를 올바르게 반영하는 것을 확인했다.

## 관련 개념
- [[concepts/parametric-memory]] — 모델 파라미터 내 암묵적 지식, non-parametric memory와 대비
- [[concepts/dense-passage-retrieval]] — non-parametric memory 검색 방법
- [[concepts/mips]] — 유사 문서 탐색 알고리즘
- [[frameworks/faiss]] — non-parametric memory 인덱싱 라이브러리
- [[patterns/index-hot-swapping]] — non-parametric memory 갱신 패턴

## 출처
- [[sources/rag-paper-lewis-2020]] — Lewis et al. (2021)
