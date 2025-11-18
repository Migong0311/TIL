
### 1. **`for...in`**

* **목적**: 객체의 **속성 이름** (키)을 순회합니다.
* **사용 예시**:

  * 객체의 키를 순회할 때 주로 사용됩니다.
  * 배열을 사용할 때는 **인덱스**(key)를 순회합니다.

```javascript
// 객체를 순회
const object = {
  a: 'apple',
  b: 'banana'
};
for (const property in object) {
  console.log(property);        // 'a', 'b' (속성 이름)
  console.log(object[property]); // 'apple', 'banana' (속성 값)
}

// 배열을 순회 (인덱스를 사용)
const numbers = [0, 1, 2, 3];
for (const index in numbers) {
  console.log(index); // 0, 1, 2, 3 (배열 인덱스)
}
```

### 2. **`for...of`**

* **목적**: 객체의 **값** 또는 배열의 **요소**를 순회합니다.
* **사용 예시**:

  * 배열이나 문자열 등의 값을 순차적으로 다룰 때 유용합니다.
  * **배열** 또는 **문자열**을 순회할 때 각 **값**을 처리합니다.

```javascript
// 배열을 순회 (값을 사용)
const numbers = [0, 1, 2, 3];
for (const number of numbers) {
  console.log(number); // 0, 1, 2, 3 (배열의 값)
}

// 문자열을 순회
const myStr = 'apple';
for (const char of myStr) {
  console.log(char); // 'a', 'p', 'p', 'l', 'e' (문자열의 문자)
}
```

### 3. **차이점**

* **`for...in`**: 객체의 **키**나 배열의 **인덱스**를 순회합니다.
* **`for...of`**: 객체의 **값**이나 배열의 **요소**를 순회합니다.

```javascript
// for...in (배열의 인덱스를 순회)
const arr = ['a', 'b', 'c'];
for (const i in arr) {
  console.log(i); // 0, 1, 2 (배열의 인덱스)
}

// for...of (배열의 값을 순회)
for (const i of arr) {
  console.log(i); // 'a', 'b', 'c' (배열의 값)
}
```


### 1. **기본 함수 매개변수 (Default Parameters)**

함수를 정의할 때, 매개변수에 기본값을 설정할 수 있습니다. 함수 호출 시 인자가 전달되지 않으면 기본값이 사용됩니다.

```javascript
const greeting = function (name = 'Anonymous') {
  return `Hi ${name}`;
}

console.log(greeting()); // Hi Anonymous
console.log(greeting('John')); // Hi John
```

* **설명**: `name` 매개변수에 기본값 `'Anonymous'`가 설정되어 있습니다. 함수 호출 시 인자가 없으면 기본값이 사용됩니다.

### 2. **나머지 매개변수 (Rest Parameters)**

`...` 연산자를 사용하여 함수에 전달된 나머지 인자들을 배열로 받을 수 있습니다. 이 방법을 통해 여러 개의 인자를 처리할 수 있습니다.

```javascript
const myFunc = function (param1, param2, ...restParams) {
  return [param1, param2, restParams];
}

console.log(myFunc(1, 2, 3, 4, 5)); // [1, 2, [3, 4, 5]]
console.log(myFunc(1, 2)); // [1, 2, []]
```

* **설명**: `...restParams`는 `param1`과 `param2` 외의 나머지 인자들을 배열로 받습니다. 예를 들어, `myFunc(1, 2, 3, 4, 5)` 호출에서 나머지 인자 `[3, 4, 5]`는 `restParams`에 배열로 저장됩니다.

### 3. **매개변수 > 인자 (매개변수의 기본값 처리)**

함수 호출 시 전달된 인자가 부족하면, 해당 매개변수는 `undefined`로 처리됩니다. 인자를 지정하지 않으면 매개변수의 기본값이 사용될 수 있습니다.

```javascript
const threeArgs = function (param1, param2, param3) {
  return [param1, param2, param3];
}

console.log(threeArgs()); // [undefined, undefined, undefined]
console.log(threeArgs(1)); // [1, undefined, undefined]
console.log(threeArgs(2, 3)); // [2, 3, undefined]
```

* **설명**: 함수 호출 시 인자가 부족하면 매개변수는 `undefined`로 처리됩니다.

### 4. **매개변수 < 인자 (넘치는 인자 처리)**

함수에 지정된 매개변수보다 더 많은 인자가 전달되면, 초과된 인자는 무시됩니다.

```javascript
const noArgs = function () {
  return 0;
}
console.log(noArgs(1, 2, 3)); // 0

const twoArgs = function (param1, param2) {
  return [param1, param2];
}
console.log(twoArgs(1, 2, 3)); // [1, 2]
```

* **설명**: `noArgs` 함수는 매개변수가 없기 때문에, 어떤 인자를 전달해도 `0`을 반환합니다. `twoArgs` 함수는 두 개의 매개변수를 가지며, 세 번째 인자는 무시되고 첫 두 인자만 사용됩니다.

### 요약




## 단축 평가 (Short-circuit Evaluation)

단축 평가는 논리 연산자(`&&`, `||`)를 사용할 때, 왼쪽 연산자가 이미 결과를 결정할 수 있으면 오른쪽 연산자는 평가하지 않는 특성을 말합니다. 이 특성은 코드 성능을 최적화하고, 불필요한 연산을 줄이는 데 유용합니다.

### 1. `&&` (AND) 연산
- **`&&` 연산**에서는 왼쪽 값이 **`false`**로 평가되면, 오른쪽 값을 평가하지 않고 결과가 `false`로 결정됩니다.
  
```javascript
console.log(1 && 0); // 0 (첫 번째 값이 truthy, 두 번째 값은 falsy)
console.log(0 && 1); // 0 (첫 번째 값이 falsy라 두 번째 값은 평가하지 않음)
console.log(4 && 7); // 7 (첫 번째 값이 truthy, 두 번째 값은 그대로 반환)
```

### 2. `||` (OR) 연산

* **`||` 연산**에서는 왼쪽 값이 **`true`**로 평가되면, 오른쪽 값을 평가하지 않고 결과가 `true`로 결정됩니다.

```javascript
console.log(1 || 0); // 1 (첫 번째 값이 truthy라 두 번째 값은 평가하지 않음)
console.log(0 || 1); // 1 (첫 번째 값이 falsy, 두 번째 값은 그대로 반환)
console.log(4 || 7); // 4 (첫 번째 값이 truthy, 두 번째 값은 평가하지 않음)
```

### 3. 단축평가 활용 예시

#### 1. **Positive 예시: 기본값 할당**

`||`를 이용해 값이 없거나 Falsy 값일 때 기본값을 할당하는 예시입니다.

```javascript
let user1 = null;
const name1 = user1 || "Guest"; // user1이 Falsy(null)이므로 "Guest"
console.log(name1); // "Guest"
```

#### 2. **Negative 예시: 의도하지 않은 기본값 할당**

숫자 `0`도 Falsy로 평가되므로, `||` 연산자에서는 `0`을 잘못된 기본값으로 취급할 수 있습니다.

```javascript
let score1 = 0; // 0점은 유효한 점수
let currentScore1 = score1 || 50; // 0이 Falsy라서 50이 할당됨 (버그 발생)
console.log(currentScore1); // 50 (원하는 값이 아닌 50이 할당됨)
```

#### 3. **해결책: 값이 `null` 또는 `undefined`일 때만 기본값 설정**

`||` 대신 조건문을 사용하여 `null`이나 `undefined`일 때만 기본값을 설정할 수 있습니다.

```javascript
let score2 = 0;
let currentScore2;

if (score2 === null || score2 === undefined) {
  currentScore2 = 50; // null이나 undefined일 때만 기본값 설정
} else {
  currentScore2 = score2;
}
console.log(currentScore2); // 0 (정상 동작)
```

### 4. **최종 (ES2020 도입) Null 병합 연산자 (Nullish Coalescing Operator) `??`**

`??` 연산자는 **`null`** 또는 **`undefined`**일 때만 오른쪽 값을 반환하며, `0`, `NaN`, `""`(빈 문자열)과 같은 Falsy 값들은 기본값으로 취급하지 않습니다.

```javascript
let score = 0;
const currentScore = score ?? 50; // score가 null이나 undefined가 아니므로 0이 그대로 사용됨
console.log(currentScore); // 0

let user = null;
const name = user ?? "Guest"; // user가 null이므로 "Guest"가 사용됨
console.log(name); // "Guest"
```

---

### 정리

* `&&`와 `||`는 **단축 평가** 특성을 활용하여 불필요한 평가를 생략할 수 있습니다.
* `||`를 사용하면 **Falsy 값**이 있을 때 기본값을 지정할 수 있지만, `0`, `NaN`, `""`와 같은 값도 **Falsy**로 평가되므로 주의해야 합니다.
* **Null 병합 연산자 `??`**는 **null**이나 **undefined**에 대해서만 기본값을 설정하고, 그 외의 Falsy 값들은 기본값을 설정하지 않으므로, 값이 `0`이나 `""`일 때 올바르게 동작합니다.
* **`for...in`**: 객체의 **속성명(키)** 또는 배열의 **인덱스**를 순회
* **`for...of`**: 배열이나 문자열의 **값** 또는 요소를 순회
* **기본값 매개변수**: 함수에서 매개변수에 기본값을 설정하여 인자가 없을 경우 기본값을 사용하도록 합니다.
* **나머지 매개변수 (`...rest`)**: 여러 개의 인자를 배열로 처리할 수 있게 해줍니다.
* **매개변수와 인자 개수 불일치**: 인자가 부족하면 매개변수는 `undefined`로 처리되며, 인자가 많으면 초과된 인자는 무시됩니다.



