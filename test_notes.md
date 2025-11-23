
# 📘 핵심 키워드 정리

| 개념                   | 설명                   | 예시                                   |
| -------------------- | -------------------- | ------------------------------------ |
| **DOM**              | HTML 문서를 객체로 표현한 것   | `document.querySelector()`           |
| **querySelector**    | CSS 선택자로 요소 하나를 선택   | `document.querySelector('.heading')` |
| **querySelectorAll** | CSS 선택자로 요소 여러 개를 선택 | `document.querySelectorAll('p')`     |
| **textContent**      | 요소의 텍스트 내용을 조작       | `h1.textContent = '수정'`              |
| **classList**        | 요소의 클래스 목록을 제어       | `h1.classList.add('red')`            |
| **setAttribute**     | 요소의 속성 값을 설정         | `a.setAttribute('href', url)`        |
| **createElement**    | 새 HTML 요소를 메모리에 생성   | `document.createElement('h1')`       |

---

# 📘 오늘 공부한 내용: 요약 및 정리

## 🔹 JavaScript 변수 선언

* JavaScript에서 변수를 선언할 수 있는 키워드는 세 가지:

  * **let**: 재할당이 가능한 변수 선언(블록 스코프)
  * **const**: 재할당 불가, 반드시 초기화 필요(블록 스코프)
  * **var**: 재선언 및 재할당 가능하지만 함수 스코프이며 호이스팅 문제로 현재는 사용 비권장

* **권장 사항:**

  * 기본적으로는 `const`를 사용
  * 재할당이 필요한 경우에만 `let`을 사용

---

# 📘 오늘 공부한 내용: 요약 및 정리

## 🔹 DOM (Document Object Model)

* DOM은 웹 페이지(Document)를 **구조화된 객체 트리 형태**로 표현한 것
* JavaScript를 통해 HTML 문서의 구조, 텍스트, 스타일 등을 **동적으로 조작**할 수 있음
* 모든 HTML 요소·속성·텍스트는 **document 객체의 하위 노드**로 구성됨 (DOM Tree)

---

## 🔹 DOM 요소 선택

* DOM 조작을 위해서는 먼저 원하는 요소를 찾아야 함

| 메서드                                   | 설명                                   |
| ------------------------------------- | ------------------------------------ |
| `document.querySelector(selector)`    | CSS 선택자와 일치하는 첫 번째 요소 반환             |
| `document.querySelectorAll(selector)` | 선택자와 일치하는 **모든 요소를 NodeList 형태**로 반환 |

---

# 📘 오늘 공부한 내용: 요약 및 정리

## 🔹 DOM 요소 조작

### ✔ 선택한 요소의 내용, 속성, 스타일 변경 또는 요소 추가/삭제 가능

---

### 1) **콘텐츠 조작**

* `textContent`
  → 요소 안의 **텍스트를 읽거나 변경**할 때 사용

---

### 2) **속성 조작**

* `classList`

  * `add`, `remove`, `toggle` 메서드로 클래스를 동적으로 제어

* `setAttribute(name, value)`
  → href, src 등 **일반 속성 값을 설정**

---

### 3) **요소 조작**

* `document.createElement(tagName)`
  → 새로운 요소를 **메모리에서 생성**

* `appendChild()`
  → 생성한 요소를 특정 부모 요소의 **마지막 자식으로 추가**

---

### 4) **스타일 조작**

* `style` 프로퍼티
  → JS로 CSS 스타일을 직접 변경


