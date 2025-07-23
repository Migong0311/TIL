# 0723 TIL 다양한 인자 종류 이론

### 1. 위치 인자

- 함수 호출 시 인자의 위치에 따라 전달되는 인자
- 위치 인자는 호출 시 반드시 값을 전달해야 함

```py
# 1. Positional Arguments
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')


greet('Alice', 25)  # 안녕하세요, Alice님! 25살이시군요.
greet(25, 'Alice')  # 안녕하세요, 25님! Alice살이시군요.
greet('Alice')  # TypeError: greet() missing 1 required positional argument: 'age'
```

### 2. 기본 인자 값

-  함수 정의에서 파라미터에 기본 값 할당
- 호출시 아규먼트 전달 않으면 디폴트 파라미터 할당

```py
# 2. Default Argument Values
def greet(name, age=20):
    print(f'안녕하세요, {name}님! {age}살이시군요.')


greet('Bob')  # 안녕하세요, Bob님! 30살이시군요.
greet('Charlie', 40)  # 안녕하세요, Charlie님! 40살이시군요.

```

### 3. 키워드 인자

- 호출시 인자의 이름과 함께 값을 전달하는 인자
- 파라미터 인자 일치안ㅅ고 특정 파라미터 값 할당 가능
- 인자의 순서 중요X 인자의 이름 명시 전달

#### 단, 호출 시 키워드 인자는 위치 인자 뒤에 위치

```py
# 3. Keyword Arguments
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')


greet(name='Dave', age=35)  # 안녕하세요, Dave님! 35살이시군요.
greet(age=35, name='Dave')  # 안녕하세요, Dave님! 35살이시군요.
greet(age=35, 'Dave')  # Positional argument cannot appear after keyword arguments

```

### 4. 임의의 인자 목록

- 정해지지 않은 개수의 인자를 처리하는 인자
- 파라미터 앞에`*`을 붙이는 것이 특징
- 여러 개의 인자를 `tuple`로 처리

```py
# 4. Arbitrary Argument Lists
def calculate_sum(*args):
    print(args)  # (1, 100, 5000, 30)
    print(type(args))  # <class 'tuple'>


calculate_sum(1, 100, 5000, 30)
```

### 5. 임의의 키워드 인자 목록

- 정해지지 않은 개수의 인자를 처리하는 인자
- 파라미터 앞에`**`을 붙이는 것이 특징
- 여러 개의 인자를 `dict`로 처리

```py
# 5. Arbitrary Keyword Argument Lists
def print_info(**kwargs):
    print(kwargs)


print_info(name='Eve', age=30)  # {'name': 'Eve', 'age': 30

```

### 함수 인자 권장 작성 순서

- 위치->기본->가변->가변 키워드

#### 단 모든 상황에 적용 절대적인 규칙 아님 상황에 따라 유연하게 조정

### 인자의 모든 종류 적용 예시


```py
# 인자의 모든 종류를 적용한 예시
def func(pos1, pos2, default_arg='default', *args, **kwargs):
    print('pos1:', pos1)
    print('pos2:', pos2)
    print('default_arg:', default_arg)
    print('args:', args)
    print('kwargs:', kwargs)


func(1, 2, 3, 4, 5, 6, key1='value1', key2='value2')
"""
pos1: 1
pos2: 2
default_arg: 3
args: (4, 5, 6)
kwargs: {'key1': 'value1', 'key2': 'value2'}
"""

```

##### © 2025 Migong0311 and SSAFY. All rights reserved.
