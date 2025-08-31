

# 📘 HTML · CSS · Bootstrap 총정리 (시험 대비용) - 9/1 삭제예정

> 시험 직전 1시간 복습용 핵심 요약
> 📌 객관식 · 주관식 · 서술형 모두 대비

---

## 1. HTML 핵심 정리

### ✅ HTML 기본 개념

* 웹 페이지의 **구조**를 정의하는 언어
* 요소(Element): 시작 태그 + 내용(Content) + 종료 태그
* 속성(Attribute): 태그에 부가 정보 추가, CSS 스타일 적용 시 활용

### ✅ HTML 기본 구조

```html
<!DOCTYPE html>
<html>
  <head>
    <title>문서 제목</title>
  </head>
  <body>
    <h1>제목</h1>
    <p>본문 내용</p>
  </body>
</html>
```

### ✅ 대표 태그

* 제목: `<h1> ~ <h6>`
* 문단: `<p>`
* 링크: `<a href="">`
* 이미지: `<img src="">`
* 구분선: `<br>`, `<hr>`

---

## 2. CSS 핵심 정리

### ✅ CSS 기본

* 웹 페이지의 **디자인과 레이아웃** 담당
* 적용 방법: 인라인, 내부(Internal), 외부(External)

### ✅ 선택자 (Selector) & 명시도

* 요소 선택자: `p { }`
* 클래스 선택자: `.class { }`
* 아이디 선택자: `#id { }`
* 명시도 우선순위: `!important > 인라인 > ID > 클래스 > 요소`

### ✅ Box Model

* Content → Padding → Border → Margin
* `box-sizing`

  * `content-box`: 기본값, 콘텐츠 크기만 width
  * `border-box`: padding + border 포함한 크기를 width로 계산

### ✅ 자주 쓰는 속성

* `margin`, `padding`, `border`
* `text-align`, `color`, `background-color`
* `display: block | inline | inline-block | none`
* `position: static | relative | absolute | fixed`
* `flex`, `justify-content`, `align-items`

---

## 3. Bootstrap 핵심 정리

### ✅ Bootstrap 특징

* 미리 정의된 CSS Framework
* Grid System 기반 반응형 레이아웃 제공
* UI 컴포넌트 (버튼, 카드, 내비게이션 등) 쉽게 사용 가능

### ✅ Grid System

* 12개의 Column으로 레이아웃 구성
* Breakpoints (화면 크기별 분기점):
  `xs < sm < md < lg < xl < xxl`

### ✅ 자주 쓰는 클래스

| 분류   | 클래스                                               | 설명                 |
| ---- | ------------------------------------------------- | ------------------ |
| 컨테이너 | `.container`, `.container-fluid`                  | 고정/가변 폭 컨테이너       |
| 그리드  | `.row`, `.col`, `.col-1`\~`.col-12`               | 행과 열 구성            |
| 반응형  | `.col-sm-*`, `.col-md-*` 등                        | 화면 크기에 따른 반응형 레이아웃 |
| 간격   | `.m-0`~~`.m-5`, `.p-0`~~`.p-5`                    | margin / padding   |
| Flex | `.d-flex`, `.justify-content-*`, `.align-items-*` | Flexbox 정렬         |
| 텍스트  | `.text-start`, `.text-center`, `.text-end`        | 텍스트 정렬             |
| 색상   | `.text-primary`, `.bg-danger`                     | 색상 스타일             |
| 버튼   | `.btn`, `.btn-primary`, `.btn-outline-*`          | 버튼 스타일             |
| 기타   | `.img-fluid`                                      | 반응형 이미지            |

---

## 4. UX · UI 정리

* **UX (User Experience)**: 사용자가 느끼는 경험과 만족도를 개선하는 디자인/개발
* **UI (User Interface)**: 사용자와 상호작용하는 화면 구성 요소

---

## 🎯 시험 예상 문제

### 1) 객관식 예상

* HTML 문서 기본 구조에 포함되지 않는 태그는?
* CSS Box Model에서 가장 바깥쪽 요소는?
* Bootstrap Grid의 기본 Column 개수는?
* Breakpoints 개수는? (정답: 6개)
* `.d-flex` 클래스의 기능은?

### 2) 주관식 예상

* **HTML, CSS, JS 역할 차이 설명**
* **Reset CSS와 Normalize CSS 차이**
* **UX와 UI 차이**
* **Bootstrap Grid System의 원리**

### 3) 서술형 예상

* **반응형 웹 디자인의 필요성**을 설명하시오.
* **CSS 명시도의 우선순위**를 순서대로 쓰시오.
* **Flexbox의 main axis와 cross axis의 차이**를 설명하시오.
* **Bootstrap의 Breakpoints의 필요성**을 설명하시오.

---

## ⏰ 시험 직전 5분 핵심 암기

1. HTML = 구조 / CSS = 디자인 / JS = 동작
2. CSS 명시도 = `!important > 인라인 > ID > 클래스 > 요소`
3. Box Model = Content → Padding → Border → Margin
4. Bootstrap Grid = 12 Columns + 6 Breakpoints
5. UX는 경험 / UI는 화면

---


#### 이상 내용은 9월1일 오후6시 이전에 삭제 할 내용입니다.

#### 이하 내용은 기존 대문 README 파일입니다

# 📚 TIL (Today I Learned)

> [![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&duration=7000&pause=800&color=15F71B&width=435&lines=A+daily+journey+of+learning+and+growth)](https://git.io/typing-svg)

이 레포지토리는 제가 매일 학습한 내용을 기록하는 공간입니다. 작고 사소하더라도 그날 배운 것을 정리함으로써 지식을 체계화하고, 꾸준한 성장을 추구합니다.

---

## ✍️ 작성 규칙

- 하루에 하나 이상의 TIL 작성
- 간결하게 요점 정리 (5~10분 내에 읽을 수 있도록)
- 코드 예제나 참고 링크는 꼭 포함
- 반복되는 내용도 다시 정리 가능 (복습 목적)

---

## 🌱 목표

- 학습한 내용을 확실히 내 것으로 만들기
- 미래의 나에게 참고 자료 제공
- 꾸준함의 힘을 체감하기

---

## 📌 참고하면 좋은 링크

- [TIL 작성 가이드 - jbranchaud/til](https://github.com/jbranchaud/til)
- [마크다운 문법 정리](https://guides.github.com/features/mastering-markdown/)

---
### 유용한 마크다운 문법

> [!NOTE]
> Useful information that users should know, even when skimming content.

> [!TIP]
> Helpful advice for doing things better or more easily.

> [!IMPORTANT]
> Key information users need to know to achieve their goal.

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.

- <ins>**밑줄예시**</ins>
```markdown
> [!NOTE]
> Useful information that users should know, even when skimming content.

> [!TIP]
> Helpful advice for doing things better or more easily.

> [!IMPORTANT]
> Key information users need to know to achieve their goal.

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.

- <ins>**밑줄예시**</ins>
```
#### 함께 공부하는 분들, 피드백은 언제든 환영합니다 🙌

##### © 2025 Migong0311 and SSAFY. All rights reserved.
