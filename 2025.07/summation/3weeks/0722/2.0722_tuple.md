# 0722 TIL 튜플 이론

## 튜플

- 어러 개의 값을 순서대로 저장하는 `불변성 시퀀스 자료형`

### 튜플 표현

- 소괄호안에 값들을 쉼표로 구분
- 모든 데이터 타입 가능
- 리스트와 비슷 그러나 `불변성`임

```py
# 튜플 표현
my_tuple_1 = ()  # 빈 튜플
my_tuple_2 = (1,)  # 요소가 하나인 케이스
my_tuple_3 = (1, 'a', 3, 'b', 5)
my_tuple_4 = 1, 'test', 3.14, True  # 괄호없어도 튜플로 인식

```

> `my_tuple_4`와 같이 괄호가 없어도 저렇게 선언하면 튜플형식으로 출력됨

#### 단 단일요소 튜플 `my_tuple_2`와 같은 경우엔 후행 쉼표를 찍어줘야함

### 튜플의 시퀀스 특징

- 시퀀스의 모든 특징과 동일함

```py
print("튜플표현\n", my_tuple_1, my_tuple_2, my_tuple_3, my_tuple_4)
my_tuple = (1, 'a', 3, 'b', 5)

# 인덱싱
print(my_tuple[1])  # a

# 슬라이싱
print(my_tuple[2:4])  # (3, 'b')
print(my_tuple[:3])  # (1, 'a', 3)
print(my_tuple[3:])  # ('b', 5)
print(my_tuple[::2])  # (1, 3, 5)
print(my_tuple[::-1])  # (5, 'b', 3, 'a', 1)

# 길이
print(len(my_tuple))  # 5
```

### 튜플의 불변성

```py
# 튜플은 불변
# TypeError: 'tuple' object does not support item assignment
my_tuple = (1, 'a', 3, 'b', 5)
my_tuple[1] = 'z'
```

### 튜플의 사용

- 불변 특성 사용해 내부 동작과 안전한 데이터 전달에 사용
- `다중할당`, `값 교환`, `함수 다중 반환 값` 등

```py

# 다중 할당
x, y = 10, 20
print(x)  # 10
print(y)  # 20
# 실제 내부 동작
# (x, y) = (10, 20)

# 값 교환
x, y = 1, 2
x, y = y, x  # 스와이핑
# 실제 내부 동작
# temp = (y, x)  # 튜플 생성
# x, y = temp  # 튜플 언패킹
# print(x, y)  # 2 1

```

> 이로 인해 안정성과 무결성 보장

##### © 2025 Migong0311 and SSAFY. All rights reserved.
