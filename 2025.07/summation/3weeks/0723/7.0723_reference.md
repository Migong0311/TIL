# 0723 TIL 참고

## 🔁 함수의 return, 반환의 원칙

* 파이썬 함수는 \*\*항상 단 하나의 값(객체)\*\*만 반환할 수 있음
* 여러 값을 `return a, b`처럼 반환하더라도 **자동으로 튜플로 패킹되어 반환**

```python
def get_user_info():
    name = 'Alice'
    age = 30
    return name, age  # 사실상 return (name, age)

user_data = get_user_info()
print(user_data)  # ('Alice', 30)
```

---

## ✅ 파이썬 함수의 반환 핵심

1. 파이썬 함수는 \*\*항상 하나의 값(객체)\*\*만 반환
2. `return a, b, c`처럼 콤마로 나열하면 → **하나의 튜플로 자동 패킹**됨
3. 반환된 튜플은 **여러 변수에 언패킹**하여 사용 가능

---

## 🔹 람다 표현식 (Lambda expressions)

* **익명 함수**를 만드는 표현식
* 한 줄로 간단한 함수 정의 가능

### 🧱 람다 표현식 구조

* `lambda` 키워드
* 매개변수 (여러 개일 경우 쉼표로 구분)
* 표현식 (반환할 연산 또는 계산)

```python
lambda x, y: x + y
```

---

## 💡 람다 표현식 예시

### 일반 함수 vs 람다 함수

```python
# 일반 함수
def addition(x, y):
    return x + y

# 람다 함수
addition = lambda x, y: x + y
```

```python
result = addition(3, 5)
print(result)  # 8
```

---

## 🔁 람다 표현식 활용 (with `map()` 함수)

```python
numbers = [1, 2, 3, 4, 5]

# 일반 함수
def square(x):
    return x**2

squared1 = list(map(square, numbers))  # [1, 4, 9, 16, 25]

# 람다 함수 사용
squared2 = list(map(lambda x: x**2, numbers))  # [1, 4, 9, 16, 25]
```

---

## 🎯 람다 표현식 활용 - 2 (with `sorted()` 함수)

> `sorted()` 함수는 리스트를 정렬하며, `key` 매개변수에 함수를 전달하여 정렬 기준 지정

### 예시: 학생을 '나이' 기준으로 정렬하기

```python
students = [(21, 90), (19, 95), (25, 85)]
```

#### ✅ 방법 1: 일반 함수 사용

```python
def get_age(student_data):
    return student_data[0]

sorted_students = sorted(students, key=get_age)
print(sorted_students)
# 출력: [(19, 95), (21, 90), (25, 85)]
```

#### ✅ 방법 2: 람다 표현식 사용

```python
sorted_students = sorted(students, key=lambda student_data: student_data[0])
print(sorted_students)
# 출력: [(19, 95), (21, 90), (25, 85)]
```

> 🎈 람다는 **한 줄짜리 기준 함수**를 즉석에서 작성할 수 있어 효율적입니다.



##### © 2025 Migong0311 and SSAFY. All rights reserved.
