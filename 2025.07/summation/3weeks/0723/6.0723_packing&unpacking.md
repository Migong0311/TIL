# 0723 TIL packing & unpacking

## packing
- 여러 개의 데이터를 하나의 컬렉션 모아 담는 과정
> 기본원리: 
여러개의 값을 하나의 tuple로 묶는 파이썬 기본 동작

>한 변수에 콤마로 구분된 값을 넣음 자동 튜플 처리



```py
packed_values = 1, 2, 3, 4, 5
print(packed_values)  # (1, 2, 3, 4, 5)

```

### `*`을 활용한 패킹

```py
# ‘*’ 을 활용한 패킹 (함수 매개변수 작성 시)
def my_func(*args):
    print(args)  # (1, 2, 3, 4, 5)
    print(type(args))  # <class 'tuple'>


my_func(1, 2, 3, 4, 5)
```


```py
# ‘**’ 을 활용한 패킹 (함수 매개변수 작성 시)
def my_func2(**kwargs):
    print(kwargs)  # {'a': 1, 'b': 2, 'c': 3}
    print(type(kwargs))  # <class 'dict’>

my_func2(a=1, b=2, c=3)
```

### 🔹 `print` 함수의 패킹 예시

* `print` 함수에서 **임의의 가변 인자**를 작성할 수 있었던 이유
  ➤ **인자 개수에 상관없이 튜플 하나로 패킹**되어 내부에서 처리되기 때문

---

### ✅ 예제 코드

```python
def my_func(*objects):
    print(objects)         # (1, 2, 3, 4, 5)
    print(type(objects))   # <class 'tuple'>

my_func(1, 2, 3, 4, 5)
# 출력:
# (1, 2, 3, 4, 5)
# <class 'tuple'>
```

---

### 💡 설명

* `*objects`는 **가변 인자**를 받는 방식으로, 여러 개의 인자들을 하나의 튜플로 **패킹(packing)** 합니다.
* 이는 `print()` 함수도 내부적으로 가변 인자를 받아 처리하는 방식과 동일합니다.


아래는 이미지 4장을 바탕으로 정리한 `Packing & Unpacking`, `*`, `**` 연산자에 대한 마크다운 정리입니다:

---

## 📦 언패킹(Unpacking)

> **컬렉션에 담겨있는 데이터를 개별 요소로 풀어 놓는 과정**

### ✅ 기본 원리

* 튜플이나 리스트 등의 객체의 요소들을 개별 변수에 할당
* '시퀀스 언패킹(Sequence Unpacking)' 또는 '다중 할당(Multiple Assignment)'이라고 부름

```python
packed_values = 1, 2, 3, 4, 5
a, b, c, d, e = packed_values
print(a, b, c, d, e)  # 1 2 3 4 5
```

---

## ✳️ `*`를 활용한 언패킹 (함수 호출 시)

> **리스트나 튜플을 개별 인자로 전달**

```python
def my_function(x, y, z):
    print(x, y, z)

names = ['alice', 'jane', 'peter']
my_function(*names)
# 출력: alice jane peter
```

---

## ✴️ `**`를 활용한 언패킹 (딕셔너리 → 함수 키워드 인자)

> **딕셔너리를 키워드 인자로 언패킹하여 전달**

```python
def my_function(x, y, z):
    print(x, y, z)

my_dict = {'x': 1, 'y': 2, 'z': 3}
my_function(**my_dict)
# 출력: 1 2 3
```

---

## 📚 Packing & Unpacking, `*` & `**` 정리

| 구분      | 상황      | `*` 연산자 사용               | `**` 연산자 사용                 |
| ------- | ------- | ------------------------ | --------------------------- |
| **패킹**  | 함수 정의 시 | 여러 위치 인자를 하나의 **튜플**로 받음 | 여러 키워드 인자를 하나의 **딕셔너리**로 받음 |
| **언패킹** | 함수 호출 시 | 리스트/튜플을 개별 **위치 인자**로 전달 | 딕셔너리를 개별 **키워드 인자**로 전달     |




##### © 2025 Migong0311 and SSAFY. All rights reserved.
