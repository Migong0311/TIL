
# 📘 CSS 시험 대비 요약 정리

시험 당일에 참고할 수 있도록 **CSS 핵심 속성**을 정리했습니다.  
내용은 이미지에서 가져온 것을 모두 포함했으며, 누락 없이 구성했습니다.

---

## 1. CSS 핵심 개념 정리

| 개념 | 설명 | 예시 |
|------|------|------|
| display 속성 | 요소의 화면 배치 방식 정의 | `.item { display: block; }` |
| position 속성 | 요소 위치를 특정 기준에 맞춰 배치 | `.box { position: absolute; }` |
| z-index 속성 | 요소의 쌓이는 순서(Z축) 정의 | `.box { z-index: 10; }` |
| CSS Flexbox | 1차원 레이아웃 배치 및 정렬 방식 | `.container { display: flex; }` |
| 주 축 방향 설정 | Flex 아이템이 나열될 방향 지정 | `flex-direction: column;` |
| 주 축 정렬 | 주 축의 아이템 정렬 및 간격 조정 | `justify-content: center;` |
| align-items | 교차 축의 아이템 한 줄 정렬 | `align-items: center;` |

---

## 2. CSS Box Model - display 속성

- **웹 페이지에서 요소가 어떻게 보이고 다른 요소와 상호작용하는지를 결정**
- **Block 타입**
  - 항상 새로운 줄에서 시작하며, 사용 가능한 전체 너비를 차지
  - 대표 태그: `<h1>~<h6>, <p>, <div>, <ul>, <li>`
- **Inline 타입**
  - 새로운 줄에서 시작하지 않고, 콘텐츠의 너비만큼 공간을 차지
  - 대표 태그: `<a>, <img>, <span>`
- **inline-block 타입**
  - inline처럼 줄바꿈 없이 다른 요소와 나란히 배치되지만, block처럼 width와 height 값 지정 가능
- **none 타입**
  - 요소를 화면에 표시하지 않으며, 레이아웃에서 차지하는 공간도 없음

---

## 3. CSS Position

- 요소를 일반적인 흐름(Normal Flow)에서 벗어나 특정 위치에 배치하는 속성

### 종류
- **static**
  - 모든 요소의 기본값, Normal Flow에 따라 배치
- **relative**
  - 자신의 원래 위치(static 위치)를 기준으로 이동
  - 이동 후에도 원래 공간은 그대로 차지
- **absolute**
  - Normal Flow에서 완전히 벗어나며, 가장 가까운 조상 요소를 기준으로 위치 결정
- **fixed**
  - absolute와 유사하나, 뷰포트를 기준으로 위치 고정

---

## 4. CSS Flexbox

- 요소를 행 또는 열의 1차원 형태로 배치하고 정렬하는 레이아웃 방식

### 핵심 구성 요소
- **Flex Container**: `display: flex;`가 적용된 부모 요소
- **Flex Item**: Flex Container의 직접 자식 요소들
- **main axis (주 축)**: Flex Item들이 배치되는 기본 축
- **cross axis (교차 축)**: 주 축에 수직인 축

---

## 5. Flex Container 관련 속성

- **flex-direction**: 아이템이 정렬될 주 축의 방향 설정 (row, column 등)
- **flex-wrap**: 아이템이 한 줄에 들어가지 않을 때 줄바꿈 여부 결정 (nowrap, wrap)
- **justify-content**: 주 축 방향으로 아이템들의 정렬과 간격 제어 (flex-start, center, space-between 등)
- **align-items**: 교차 축 방향으로 한 줄의 아이템들을 정렬 (stretch, flex-start, center 등)
- **align-content**: 여러 줄의 아이템이 있을 때 교차 축 방향으로 줄들의 간격과 정렬 제어

---

## 6. Flex Item 관련 속성

- **flex-grow**: 컨테이너에 여유 공간이 있을 때 아이템이 늘어나는 비율 지정
- **flex-basis**: 아이템의 초기 크기 설정
- **align-self**: 특정 아이템 하나만 개별적으로 교차 축 정렬 변경 가능

---

✅ 이 문서는 시험 당일 참고용으로 제작되었습니다.
