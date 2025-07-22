# 0722 TIL etc type 이론

### None

- null이랑 같음
- `a = 0`, `b = ''` 이건 none 이 아니라 값이 존재하는거임

```py
a=None
print(a) # None
```

### Boolean

- 논리형 타입
  ![image.png](/2025.07/summation/3weeks/0722/0722_images/image.png)

### Collection

- 여러개의 값을 하나로 묶어 관리하는 자료형 통칭 의미
  ![image.png](/2025.07/summation/3weeks/0722/0722_images/image-2.png)

## _중요!!_

| 컬렉션명 | 변경 가능 여부 | 순서 존재 여부 | 분류     |
| -------- | -------------- | -------------- | -------- |
| `str`    | ❌             | ✅             | 시퀀스   |
| `list`   | ✅             | ✅             | 시퀀스   |
| `tuple`  | ❌             | ✅             | 시퀀스   |
| `dict`   | ✅             | ❌             | 비시퀀스 |
| `set`    | ✅             | ❌             | 비시퀀스 |

### 불변 가변

| 구분 | 불변 (Immutable)             | 가변 (Mutable)            |
| ---- | ---------------------------- | ------------------------- |
| 특징 | 변경 불가, 안전성, 예측 가능 | 변경 가능, 유연성, 효율성 |
| 종류 | `str`, `tuple`, `range`      | `list`, `dict`, `set`     |

### 형변환

- 한 데이터 타입을 다른 데이터 타입으로 변환하는 과정

### 암시적 형변환

- 파이썬이 자동적으로 형변환해주는거
- Boolean과 정수에서만 가능

```py
# 암시적 형변환
# 정수(int)와 실수(float)의 덧셈
print(3 + 5.0)  # 8.0
# 불리언(bool)과 정수(int)의 덧셈
print(True + 3)  # 4
# 불리언간의 덧셈
print(True + False)  # 1
```

### 명시적 형변환

- 개발자가 직접 형변환 해주는거

```py
# 명시적 형변환
# str -> int
print(int('1'))  # 1
# ValueError: invalid literal for int() with base 10: '3.5'
# print(int('3.5'))
print(int(3.5))  # 3
print(float('3.5'))  # 3.5

# int -> str
print(str(1) + '등')  # 1등
```

### 명시적 형변환 예시

| 함수      | 설명          | 예시            | 결과              |
| --------- | ------------- | --------------- | ----------------- |
| `int()`   | 정수로 변환   | `int("123")`    | `123`             |
| `float()` | 실수로 변환   | `float("3.14")` | `3.14`            |
| `str()`   | 문자열로 변환 | `str(100)`      | `"100"`           |
| `list()`  | 리스트로 변환 | `list("abc")`   | `['a', 'b', 'c']` |
| `tuple()` | 튜플로 변환   | `tuple([1,2])`  | `(1, 2)`          |
| `set()`   | 세트로 변환   | `set([1,2,2])`  | `{1, 2}`          |

##### © 2025 Migong0311 and SSAFY. All rights reserved.
