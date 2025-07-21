# 0721 TIL sequence type 이론

## sequence type

- 여러 개의 값들을 **순서**대로 **나열**하여 저장하는 자료형
  > str, list,tuple,range

### index

- 시퀀스 자료형에서 각 값의 위치를 식별하기 위해 부여된 고유의 번호
  > 시작은 1번이 아닌 **0번**부터 시작함

### 시퀀스 타입의 공통 특징

1. 순서

- 값들이 순서대로 저장 (**정렬 X**)

2. 인덱싱

- 각 값의 고유 번호를 가지고 있으며 인덱스를 사용 특정 위치의 값을 선택,수정이 가능하다.

3. 슬라이싱

- 인덱스 범위를 조절해 전체 데이터 중 원하는 부분만 값을 잘라내서 사용 가능

4. 길이

- `len()` 함수 사용하여 저장된 값의 개수를 구할 수 있음

5. 반복

- 반복문을 사용하여 각 값을 하나씩 순서대로 꺼내 사용 가능

### 시퀀스 타입 특징 예시

- my_data="Hello" 라는 문자열 데이터가 있을 때
  ![image.png](/2025.07/summation/3weeks/0721/0721_images/image-12.png)

## str(문자열)

```python
print('Hello World!')
print("Hello World!")

```

- 큰 따옴표 혹은 작은 따옴표 사용 가능 단 위에 예시로직 처럼 한 로직들 안에서 혼용 사용 금지
- 한 문자열 안에 따옴표를 사용할 경우 본래 감쌌던 따옴표에 반대 따옴표로 감싸면 됨

### 특수 표현

1. \(역슬레시)

```python
print("It\'s a good time")
```

2. \n(개행)

```python
print("It\'s a \n good time")
```

3. """(여러 행 출력)

```python
str = """
동해물과 백두산이
마르고 닳도록
하느님이 보우하사 ...
"""
print(str)
```

![image.png](/2025.07/summation/3weeks/0721/0721_images/image-13.png)

### f-string

![image.png](/2025.07/summation/3weeks/0721/0721_images/image-14.png)

## 인덱스

- 시퀀스 자료형에서 각 값의 위치를 식별하기 위해 부여된 번호

```python
# 문자열의 시퀀스 특징
my_str = 'hello'
# 1. 인덱싱
print(my_str[1])  # e
```

![image.png](/2025.07/summation/3weeks/0721/0721_images/image-15.png)

- 위에 예시코드처럼 해당하는 인덱스를 대괄호로 넣으면 h가아닌e가 출력됨

### 슬라이싱

- 대괄호 안에 시작 위치,끝위치,긴격을 콜론으로 구분

```python
변수명[start:stop:step]
```

1. start : 슬라이싱을 시작할 인덱스
2. stop : 슬라이싱을 끝낼 인덱스 (**포함X**)
3. step : 몇 개씩 건너뛰며 값을 가져올지에 대한 간격

```python
print(my_str[2:4]) # ll
print(my_str[:3]) # hel
print(my_str[3:]) # lo
print(my_str[::2]) # hlo
print(my_str[::-1]) # olleh
```

1. `print(my_str[2:4])` 이 경우엔 2번 즉 'l'부터4번 전까지인 'l'까지 끊는다는 의미 (step은 0이기 때문에 생략)
   > ll
2. `print(my_str[:3])` 이경우엔 start값이 0이라 생략된 케이스 즉 2번까지 출력
   > hel
3. `print(my_str[3:])` 2번 예제랑 반대케이스 즉 stop값이 생략되며 인덱스가 총 4번까지이기 때문에 생략되면 그냥 마지막 인덱스까지 출력이라고 생각하면 됨
   > lo
4. `print(my_str[::2])` 콜론이 2개인경우 start랑stop값이 생략된 케이스 즉 2번이랑 3번을 합친 케이스에 step값이 2 즉 0번부터 2칸 단위로 출력
   > hlo
5. `print(my_str[::-1])` 위랑 동일한 케이스이나 음수인덱스는 0번자리에 가까워질수록 음수값도 작아지기때문에 즉 반대로 출력 하는 의미
   > ![image.png](/2025.07/summation/3weeks/0721/0721_images/image-16.png)

### 문자열의 불변성

- 문자열은 한번 선언하면 불변성 즉 immutable 성질을 지님

```python
exam='hello'
exam[1]='a'
```

- 위와 같이 exam변수를 hello로 지정했으나 1번 인덱스를 a로 임의 변경시 런타임 에러가 발생한다

### 변환을 하고싶으면

![image.png](/2025.07/summation/3weeks/0721/0721_images/image-17.png)

- 위와 같이 **재정의**를 해줘야함
