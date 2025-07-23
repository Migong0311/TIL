# 0723 TIL 함수와 스코프 정리

## 파이썬의 범위 - Scope

- 함수 코드 내부는 `local scope`, 그 외는 `global scope`로 구분

### 범위와 변수 관계

- scope
    - global scope: 로직 어디서든 참고가능 공간
    - local scope: 함수 내부에서만 참고 가능 공간
- variable
    - global variable: global scope에 정의된 변수
    - local variable: local scope에 정의된 변수

### 예시

```py
# Scope 예시
def func():
    num = 20
    print('local', num)  # local 20


func()

print('global', num)  # NameError: name 'num' is not defined

```

- 위 변수는 함수내에선 동작 그러나 아래 전역에선 사용 불가 
- 이는 변수의 수명주기와 연관 있음


### 🔵 변수 수명주기(lifecycle)

* 변수의 수명주기는 **변수가 선언되는 위치와 scope**에 따라 결정됨

---

1. **built-in scope**

   * 파이썬이 실행된 이후부터 **영원히 유지**

2. **global scope**

   * **모듈이 호출된 시점 이후** 혹은 **인터프리터가 끝날 때까지 유지**

3. **local scope**

   * **함수가 호출될 때 생성**되고, **함수가 종료될 때까지 유지**


### 이름 검색 규칙

- 아래와 같은 순서로 이름을 찾아 나가며 `LEGB rule`이라고 부름

1. Local scope: 지역범위 현재 내가 작업중인 곳
2. Enclosed scope: 지역범위 주로 이중 함수일경우 상위 함수 공간
3. Global scope: 최상단 전역 변수
4. Built-in scope: 내장 함수

<!-- 46p 사잔 -->
  ![image.png](/2025.07/summation/3weeks/0723/image/image-4.png)

### 예시

```python
print(sum(range(3)))  # TypeError: 'int' object is not callable
```

이 부분이 오류가 발생하는 **핵심 원인**은 **`sum`이라는 이름을 내장 함수로서가 아니라 정수 `int` 값으로 덮어썼기 때문**.

---

## 🔍 순서대로 분석해보면:

```python
print(sum)  # <built-in function sum>
```

→ 이 시점에서 `sum`은 파이썬의 내장 함수입니다.
→ 따라서 `sum(range(3))`은 정상적으로 작동하며 `0 + 1 + 2 = 3`을 출력.

```python
sum = 5
print(sum)  # 5
```

→ 여기서 `sum`이라는 이름에 **정수 값 5를 할당**하면서, 더 이상 `sum()`이라는 **함수**가 아니라 **정수**로 취급.

---

## ⚠️ 문제의 코드

```python
print(sum(range(3)))  # TypeError: 'int' object is not callable
```

이 줄에서 `sum`은 이제 `5`이기 때문에, `sum(range(3))`은 **정수(5)를 함수처럼 호출하려고 한 꼴**.

### 따라서:

* `range(3)` → \[0, 1, 2]
* `sum` → `5` (int)
* `5([0, 1, 2])` ← 이걸 실행하려 하니 `TypeError: 'int' object is not callable` 오류가 발생하는 것.

---

## ✅ 해결 방법

내장 함수의 이름을 변수 이름으로 사용하지 말고, 다른 이름을 사용해야함:

```python
my_sum = 5  # OK
print(sum(range(3)))  # 정상 작동
```

또는 덮어쓴 이후에는 원래 내장 함수에 접근할 수 없기 때문에 \*\*재시작하거나 `del`\*\*로 삭제해줘야 함:

```python
del sum
print(sum(range(3)))  # 다시 정상 작동
```

### LEGB Rule 퀴즈

```py
# LEGB Rule 퀴즈
x = 'G'
y = 'G'


def outer_func():
    x = 'E'
    y = 'E'

    def inner_func(y):
        z = 'L'
        print(x, y, z)  # ??

    inner_func('P')
    print(x, y)  # ??


outer_func()
print(x, y)  # ??

```

<!-- 50p 사진 -->
  ![image.png](/2025.07/summation/3weeks/0723/image/image-5.png)

### global 키워드

- 변수의 스코프를 전역 범위 지정 목적
- 일반적으로 함수 내에서 전역 변수 수정 희망시 사용

```py
num = 0  # 전역 변수


def increment():
    global num  # num를 전역 변수로 선언
    num += 1


print(num)  # 0

increment()

print(num)  # 1
```

### 주의 사항

1. global 키워드 선언 전 참조불가

```py
# ‘global’ 키워드 주의사항 - 1
# global 키워드 선언전에참조불가
num = 0


def increment():
    # SyntaxError: name 'num' is used # prior to global declaration
    print(num) # ㅜ
    global num # ㅗ
    num += 1


```

2. 파라미터엔 사용 불가

```py
# ‘global’ 키워드 주의사항 - 2
# 매개변수에는 global 키워드 사용불가
num = 0


def increment(num):
    # "num" is assigned before global # declaration
    global num
    num += 1

```


##### © 2025 Migong0311 and SSAFY. All rights reserved.
