# 0721 TIL data type 이론

## 타입

- 타입이란 변수나 값이 가질 수 있는 데이터의 종류
  > 타입엔 값(피연산자)랑 연산자(+,-,\*)로 나뉨

## Data Type

- 값의 종류와 그 값으로 할 수 이쓴ㄴ 동작을 결정하는 속성

  > 어떤 데이터가 주어졌을 때 컴퓨터에게 이것은 무엇이다 라고 알려주는 명세서

- 필요 이유는 각 타입에 따라 가능한 기능과 연산이 다르기 때문
  > 예 : `3+4=7`, `"나"+"너"=나너` 는 가능
  > ~~`3+"너"=ERROR`~~ 이렇게 타입이 다른 연산은 불가능

### Data Type 분류

1. Numeric Types
   > 예 : 12->정수헝(int), 0.1->실수형(float)
2. Text Sequence Types
   > 예 : "string"->문자열(string)
3. Sequence Types
   > list, tuple,range
4. Non-Sequence Types
   > set,dict
5. 기타
   > boolean,None

### 1. Numeric Types

### 지수 표현법

```python
#1,230,000,000
big_number = 1.23e9

# 0,00314
small_number = 3.14e-3
```

- 위 예시처럼 e를 사용

### 산술연산자

![image.png](/2025.07/summation/3weeks/0721/0721_images/image-10.png)

#### 우선순위는 `거듭제곱(**)`,`음수부호`,`곱셈`,`나눗셈`,`정수나눗셈`,`나머지` 그리고 `덧셈`,`뺼셈`임

![image.png](/2025.07/summation/3weeks/0721/0721_images/image-11.png)

- 위 예제처럼 1번은 본래 수학적으론 16이 맞지만 우선순위에 의해 -16이 됨
- 그래서 2번째 또는 3번째 예제처럼 괄호를 설정하여 임의로 우선순위를 지정해줘야 원하는 값을 도출할 수 있음

##### © 2025 Migong0311 and SSAFY. All rights reserved.
