# 0723 TIL 함수 이론

## 함수

- 특정 작업을 수행하기 위한 **재사용 가능한 코드 묶음**

### 함수 사용 이유

- 코드의 중복 방지
- 재사용성 높아지고 코드의 가독성및 유지보수성 향상

```py
#before

a = 1
b = 2

result = a + b
print(result)
```
- 이래하면 값이 달라질때 마다 계속 이래야됨

```py
# after

def get_sum(a,b):
    return a + b

a = 5
b = 3
result = get_sum(a,b)
print(result)
```

### 함수호출

- 함수 실행 위해 함수의 이름을 사용 해당 함수 코드 블록 실행
- 바로 위 로직에서 `result = get_sum(a,b)` 이 로직이 호출하는거


### 함수구조
```py
def make_sum(param1, param2):
    """이것은 두 수를 받아
    두 수의 합을 반환하는 함수입니다.
    >>> make_sum(1,2)
    3
    """
    return param1+param2
```
<!-- 11p 캡쳐 -->
  ![image.png](/2025.07/summation/3weeks/0723/image/image.png)

<!-- 12p 캡쳐 -->
  ![image.png](/2025.07/summation/3weeks/0723/image/image-1.png)


- parameter: 함수에 희망하는 Input 값
- Docstring: 함수에 대한 설명(JavaDoc이랑 동일)
- function body: 함수 내용에 대한 정의 return 문 포함
- return: 함수의 실행값을 반환(Output)하며 함수의 실행이 종료된다. 

### 함수 정의와 호출

- 함수 정의는 `def`키워드로 시작
- 괄호안에 파라미터 정의

```py
def make_sum(param1, param2):
    """이것은 두 수를 받아
    두 수의 합을 반환하는 함수입니다.
    >>> make_sum(1,2)
    3
    """
    return param1+param2
```

- 함수 body는 콜론 담에 **들여쓰기(tab키 1번)**

<!-- 14p 캡쳐 -->
  ![image.png](/2025.07/summation/3weeks/0723/image/image-2.png)

- Docstring : 함수 body 앞에 선택적 작성 가능 함수 설명서
<!-- 15p 캡쳐 -->
  ![image.png](/2025.07/summation/3weeks/0723/image/image-3.png)

- 함수 반환값 : 필요시 결과 반환 가능 `return`문으로 키워드 작성 후 결과를 호출 부분으로 반환

> 단 return이 없으먼 default는`None`

- 함수 호출 : 함수사용 위해 호출 필요 이름 및 소괄호 호출 필요시 파라미터 값을 인자값으로 전달

```py
def make_sum(param1, param2):
    """이것은 두 수를 받아
    두 수의 합을 반환하는 함수입니다.
    >>> make_sum(1,2)
    3
    """
    return param1+param2
    # 또는 result =  param1+param2
    # return result 이런식으로도 가능


# 함수 호출 및 반환 값 할당
result = make_sum(100, 30)
print(result)
```

### 함수와 반환 값

- print()함수는 화면에 값 **`출력`** 역할만 존재 반환값은 없음 ->default는 None이기 때문


```py
# print() 함수는 반환값이 없다.
result_value = print()
print(result_value)  # None
```

> 실제로 출력해 본 결과 None이나옴
> print함수에 출력값을 입력하여도 출력값이 존재하는거지 반환되는건 여전히 없음

## 매개변수 VS 인자

### 매개변수

- 함수를 정의할 때 함수가 받을 값을 나타내는 변수


```py
def add_numbers(x, y):  # x와 y는 매개변수
    result = x + y
    return result
...
```

### 인자 

- 함수를 호출할 때 실제로 전달되는 값

```py
...
a = 2
b = 3

sum_result = add_numbers(a, b)  # a와 b는 인자
print(sum_result)  # 5

```

##### © 2025 Migong0311 and SSAFY. All rights reserved.
