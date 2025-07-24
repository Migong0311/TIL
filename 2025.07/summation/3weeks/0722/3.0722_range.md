# 0722 TIL range 이론

## range

- `연속된 정수 시퀀스`를 생성하는 `불변성` 자료형
- 주로 반복문에 특정 횟수 반복 시 많이 사용

### range 기본 구문

```py
range(start,stop,step)
```

> range()는 1개2개 또는 3개의 파라미터 가질 수 있음 약간 인덱스 슬라이싱 느낌

```py
# range 표현
my_range_1 = range(5)
my_range_2 = range(1, 10)
my_range_3 = range(5, 0, -1)

print(my_range_1)  # range(0, 5)
print(my_range_2)  # range(1, 10)
print(my_range_3)  # range(5, 0, -1)

# 리스트로 형 변환 시 데이터 확인 가능
print(list(my_range_1))  # [0, 1, 2, 3, 4]
print(list(my_range_2))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(my_range_3))  # [5, 4, 3, 2, 1]
```

- range(stop)
  - 파라미터 1개면 stop으로 인식
  - start는 0,step은 1 default
    > 슬라이싱은 전부 0이 default 였지만 여기선 step이 생략시 1로 고정
- range(start,stop)
  - 2개일경우
  - step 1 default
- range(start,stop,step)
  - 모든 파라미터 커스텀

> 실제로 range에 파라미터 값을 확인 희망 시 형변환 하셈

### range 규칙

### 1. 값의 범위 규칙

- stop 값은 생성되는 시퀀스에 절대 포함 X
- range(1,5)면 `[1,2,3,4]`로 출력(슬라이싱이랑 동일)

### 2. 증가/감소 값(step) 규칙

- step 값은 숫자 시퀀스의 간격과 방향 결정

#### 1. step값 양수

- start ++ -> stop
  > 단 시작 값이 끝 값보다 큰 경우 빈리스트 반환 -> 에러는 아님

```py

# 증가/감소 값(step) 규칙

# step이 양수일 때 (기본값 1)
# 시작 값이 끝 값보다 작은 경우 (정상)
print(list(range(1, 5)))  # [1, 2, 3, 4]
# 시작 값이 끝 값보다 큰 경우
print(list(range(5, 1)))  # []

```

#### 2. step 음수

- start -- -> stop
- **start > stop**(아닐경우 동일하게 빈 리스트)

```py
# step이 음수일 때
# 시작 값이 끝 값보다 큰 경우 (정상)
print(list(range(5, 1, -1)))  # [5, 4, 3, 2]
# 시작 값이 끝 값보다 작은 경우
print(list(range(1, 5, -1)))  # []
```

### range 에시

```py
# 주로 반복문과 함께 활용 예정
for i in range(1, 10):
    print(i)  # 1 2 3 4 5 6 7 8 9

for i in range(1, 10, 2):
    print(i)  # 1 3 5 7 9
```

##### © 2025 Migong0311 and SSAFY. All rights reserved.
