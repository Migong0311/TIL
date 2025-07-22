# 0722 TIL dict & set 이론

## dict(딕셔너리)

- `key-value` 쌍으로 이루어진 순서와 중복이 없는 `변경 가능 자료형`

### 딕셔너리 표현

- 중괄호 안에 값들이 쉼표로 구분
- 값 1개는 키와 값이 쌍으로 이뤄저있음 중간에 콜론으로 구분
- key - 값을 식별하기 위한 이름 **(중복 X)**
- Value - 키에 해당하는 실제 데이터
- 각 값에는 순서 X

```py
# 딕셔너리 표현
my_dict_1 =  {}
my_dict_2 = {'key': 'value'} # key - value 쌍으로 사이에 콜론 처리
my_dict_3 = {'apple': 12, 'list': [1, 2, 3]}

print(my_dict_1)  # {}
print(my_dict_2)  # {'key': 'value'}
print(my_dict_3)  # {'apple': 12, 'list': [1, 2, 3]}

```

> 단 3.7버전 부터는 개발자의 순서에 맞게 출력해줌 그러나 순서가 생긴건 아님

### 딕셔너리 규칙(key)

1. 고유성
2. 불변성 자료형만 사용 가능

### 딕셔너리 규칙(Value)

- 어떤 자료형이든 자유롭게 사용 가능

### 딕셔너리 값 접근

- key를 사용 해당 value 꺼내기 가능
- 접근시 대괄호 활용
  > 단 존재하지 않는 key 값을 출력할 시 keyError 발생

```py
# 딕셔너리는 키에 접근해 값을 얻어냄
my_dict = {'name': '홍길동', 'age': 25}
print(my_dict['name'])  # '홍길동'
print(my_dict['test'])  # KeyError: 'test'

```

### 딕셔너리 값 추가 및 변경

```py
# 딕셔너리 값 추가 및 변경
my_dict = {'apple': 12, 'list': [1, 2, 3]}
# 추가
my_dict['banana'] = 50
print(my_dict)  # {'apple': 12, 'list': [1, 2, 3], 'banana': 50}

# 변경
my_dict['apple'] = 100
print(my_dict)  # {'apple': 100, 'list': [1, 2, 3], 'banana': 50}

```

> 데이터 순서 필요없거나 각 데이터에 의미있는 이름을 붙여 관리하고 싶을때 사용

---

## set

- 순서와 중복이 없는 `변경 가능한 자료형`

### set 표현

- 중괄호 안에 값들을 콤마로 구분
- 수학에서 *집합*과 동일한 연산 처리 가능

### 특징

- 중복 허용 않음
- 순서 없음

```py
# 세트 표현
my_set_1 = set()
my_set_2 = {1, 2, 3}
my_set_3 = {1, 1, 1}

print(my_set_1)  # set()
print(my_set_2)  # {1, 2, 3}
print(my_set_3)  # {1}
```

### set위 집합 연산

- set는 수학 집합 개념 그대로 가져와 두 데이터 그룹 간의 관계를 파악하는데 매우 효과적

```py
# 세트의 집합 연산산
my_set_1 = {1, 2, 3}
my_set_2 = {3, 6, 9}

# 합집합
print(my_set_1 | my_set_2)  # {1, 2, 3, 6, 9}

# 차집합
print(my_set_1 - my_set_2)  # {1, 2}

# 교집합
print(my_set_1 & my_set_2)  # {3}
```

##### © 2025 Migong0311 and SSAFY. All rights reserved.
