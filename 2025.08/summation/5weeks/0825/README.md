
# 📘 HTML & CSS 핵심 키워드 및 요약 정리

시험 대비용으로 HTML과 CSS의 핵심 개념을 정리했습니다.

---

## 1. 핵심 키워드

| 개념 | 설명 | 예시 |
|------|------|------|
| 웹 페이지 (Web Page) | 웹 사이트를 구성하는 요소 | 홈페이지, About Us 등 |
| HTML | 웹 페이지의 구조를 정의 | `<h1>Title</h1>` |
| CSS | 웹 페이지의 디자인을 구성 | `h1 { color: red; }` |
| CSS 선택자 (Selector) | 스타일을 적용할 요소를 선택 | `.classname` |
| 명시도 (Specificity) | 스타일 적용 우선순위 규칙 | `ID > class > 요소` |
| CSS Box Model | HTML 요소를 감싸는 상자 | margin, border, ... |
| 단축 속성 (shorthand) | 여러 속성을 한 번에 설정 | `margin: 10px 20px;` |

---

## 2. 웹(Web)의 기본 개념

- **World Wide Web (WWW)**은 인터넷을 통해 정보를 공유하는 거대한 공간입니다.  
- 웹 페이지는 HTML, CSS 등으로 만들어진 웹 사이트의 개별 요소이며, 이러한 웹 페이지들이 모여 웹 사이트를 구성합니다.  
- 웹 페이지는 **HTML(구조), CSS(스타일), JavaScript(동작)** 세 가지 요소로 이루어집니다.  

---

## 3. HTML (HyperText Markup Language)

- HTML은 **웹 페이지의 의미와 구조를 정의하는 언어**입니다.  
- **HyperText**: 다른 페이지로 이동할 수 있는 링크를 의미  
- **Markup Language**: 태그를 사용해 문서 구조를 명시하는 언어  
- **요소(Element)**: 태그와 그 안의 내용으로 구성  
- **속성(Attribute)**: 요소에 추가 정보를 부여하며, CSS에서 스타일 적용 시 활용  

---

## 4. CSS (Cascading Style Sheets)

- CSS는 **웹 페이지의 디자인과 레이아웃**을 담당하는 언어입니다.

### 적용 방법
- **인라인(Inline)**: `<h1 style="color: blue;">`처럼 요소에 직접 적용  
- **내부(Internal)**: `<style>` 태그를 `<head>` 안에 넣어 사용  
- **외부(External)**: `.css` 파일을 만들어 `<link>` 태그로 연결 (유지보수에 효율적)  

### CSS 선택자와 명시도
- **선택자(Selector)**: HTML 요소를 선택하여 스타일 적용  
  - 기본 선택자: 전체(`*`), 요소(`h1`), 클래스(`.class`), 아이디(`#id`)  
  - 결합자: 자손(` `)이나 자식(`>`) 요소 선택 가능  
- **명시도(Specificity)**: 여러 규칙 충돌 시 적용될 우선순위를 결정하는 알고리즘  
  - 순위: `!important` > 인라인 스타일 > `#id` > `.class` > 요소  

---

## 5. CSS Box Model

- 모든 HTML 요소는 **Content, Padding, Border, Margin**으로 구성된 사각형 상자 모델을 가집니다.  
- **box-sizing** 속성으로 너비와 높이 계산 방식을 제어합니다.  
  - **content-box (기본값)**: width는 콘텐츠 영역의 너비만 의미  
  - **border-box**: width가 테두리와 안쪽 여백을 포함한 전체 박스 너비가 됨 → 레이아웃 관리가 더 직관적  

---

✅ 이 문서는 시험 당일 빠르게 참고할 수 있도록 작성되었습니다.
