# 0723 TIL style guide 이론

### 함수명 작성 규칙

- 소문자,언더바 사용
- 동사 시작 함수
- 약어 사용 지향


```py
# Good
def calculate_total_price(price, tax):
    return price + (price * tax)


# Bad
def calc_price(p, t):
    return p + (p * t)

```


### 🔷 단일 책임 원칙 (Single Responsibility Principle)

* 모든 객체는 **하나의 명확한 목적과 책임**만을 가져야 함

---

### 🧩 함수 설계 원칙

1. **명확한 목적**

   * 함수는 **한 가지 작업만 수행**
   * 함수 이름으로 목적을 명확히 표현

2. **책임 분리**

   * 데이터 검증, 처리, 저장 등을 **별도 함수로 분리**
   * 각 함수는 **독립적으로 동작** 가능하도록 설계

3. **유지보수성**

   * 작은 단위의 함수로 나누어 관리
   * 코드 수정 시 **영향 범위를 최소화**



### 잘못된 설계 예시

```py
# 잘못된 설계 예시 (여러 책임이 섞인 함수)
def process_user_data(user_data):
    # 책임 1: 데이터 유효성 검사
    if len(user_data['password']) < 8:
        raise ValueError('비밀번호는 8자 이상이어야 합니다')

    # 책임 2: 비밀번호 암호화 및 저장
    user_data['password'] = hash_password(user_data['password'])
    db.users.insert(user_data)

    # 책임 3: 이메일 발송
    send_email(user_data['email'], '가입을 환영합니다!')



```

### 올바른 설계 예시
```py
# 올바른 설계 예시 (책임을 분리한함수들)
def validate_password(password):
    """비밀번호 유효성 검사"""
    if len(password) < 8:
        raise ValueError('비밀번호는 8자 이상이어야 합니다')


def save_user(user_data):
    """비밀번호 암호화 및 저장"""
    user_data['password'] = hash_password(user_data['password'])
    db.users.insert(user_data)


def send_welcome_email(email):
    """환영 이메일 발송"""
    send_email(email, '가입을 환영합니다!')


# 메인 함수에서 순차적으로 실행
def process_user_data(user_data):
    validate_password(user_data['password'])
    save_user(user_data)
    send_welcome_email(user_data['email'])

```

##### © 2025 Migong0311 and SSAFY. All rights reserved.
