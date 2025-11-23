아래는 **이벤트 관련 핵심 개념 전체를 마크다운 형식으로 깔끔하게 정리한 자료**입니다.
(사용자가 제공한 표 + 설명 모두 포함한 통합 정리본)

---

# 📌 이벤트(Event) 핵심 정리 (Markdown)

## 🟦 1. 이벤트 기본 개념

### ✔ 이벤트(Event)

* 웹페이지에서 사용자의 **클릭, 키보드 입력, 마우스 움직임** 등 ‘무언가 일어났음’을 의미하는 **신호 또는 사건**
* **예시:** `click`, `input`, `keydown` 등

---

### ✔ 이벤트 객체(event object)

* 이벤트가 발생하면 **자동 생성**되는 객체
* 이벤트에 대한 상세 정보 포함
  (마우스 좌표, 입력 키, 발생 위치 등)

---

### ✔ 이벤트 핸들러(event handler)

* **특정 이벤트 발생 시 실행되도록** 등록된 콜백 함수
* 예시:

```js
btn.addEventListener('click', func)
```

---

### ✔ addEventListener(type, handler)

* DOM 요소에 **특정 이벤트 타입(type)**이 발생했을 때 실행할 **핸들러 함수를 등록**
* 예시:

```js
btn.addEventListener('click', func)
```

---

## 🟦 2. 이벤트 버블링(Event Bubbling)

### ✔ 이벤트 버블링이란?

* 한 요소에서 이벤트가 발생하면
  → 해당 요소의 핸들러 실행
  → **부모 요소 → 조상 요소 순으로 전파되는 현상**

---

### ✔ event.target vs event.currentTarget

#### 🟩 event.target

* **이벤트가 실제로 처음 발생한 가장 안쪽 요소(시작 지점)**
* 버블링이 진행되어도 **변하지 않음**
* 예시:

```js
console.log(event.target)
```

#### 🟩 event.currentTarget

* 현재 **핸들러가 연결된 요소** (= this 와 동일)
* 예시:

```js
console.log(event.currentTarget)
```

---

### ✔ preventDefault()

* 요소의 **기본 동작을 취소**
* 예시: 링크 이동, form 제출 방지

```js
event.preventDefault()
```

---

## 🟦 3. 핵심 개념 표 정리

| 개념                      | 설명                   | 예시                                    |
| ----------------------- | -------------------- | ------------------------------------- |
| **이벤트(event)**          | 웹페이지에서 일어나는 신호 또는 사건 | click, input                          |
| **이벤트 핸들러**             | 이벤트 발생 시 실행되는 콜백 함수  | `btn.addEventListener('click', func)` |
| **addEventListener**    | DOM 요소에 이벤트 핸들러를 등록  | `btn.addEventListener('click', func)` |
| **이벤트 버블링**             | 이벤트가 부모 요소로 전파되는 현상  | 하위 요소 클릭 시 상위 요소 핸들러도 실행              |
| **event.target**        | 이벤트가 시작된 요소          | `console.log(event.target)`           |
| **event.currentTarget** | 핸들러가 연결된 요소          | `console.log(event.currentTarget)`    |
| **preventDefault**      | 요소의 기본 동작 취소         | `event.preventDefault()`              |

---

# ✔ 전체 요약

* **이벤트(event)**: 웹에서 발생하는 사건 (click 등)
* **이벤트 핸들러**: 이벤트 발생 시 실행할 함수
* **addEventListener**: 이벤트를 요소에 등록하는 메서드
* **버블링**: 이벤트가 부모 방향으로 전파되는 과정
* **event.target**: 이벤트가 실제 발생한 요소
* **event.currentTarget**: 핸들러가 연결된 요소
* **preventDefault()**: 기본 동작 취소

---

필요하시면 **문제·정답 포함한 시험버전 요약**,
또는 **퀴즈 형태 PDF**, **훈련용 문제세트**로도 제작해 드리겠습니다!
