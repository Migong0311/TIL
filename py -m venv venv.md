# 📝 Django 가상환경 & 프로젝트 세팅 정리

## 1️⃣ 가상환경 생성 & 실행

```bash
# 가상환경 생성
py -m venv venv

# 가상환경 활성화 (Windows PowerShell)
source venv/Scripts/activate
```

---

## 2️⃣ 패키지 설치

### (A) 새 프로젝트 시작 시

```bash
pip install django ipython
pip freeze > requirements.txt
```

### (B) 기존 프로젝트 이어받을 때

```bash
pip install -r requirements.txt
```

---

## 3️⃣ 프로젝트 & 앱 생성

```bash
# 프로젝트 생성 (현재 디렉토리에 생성)
django-admin startproject library_management .

# 앱 생성 (복수형 권장)
py manage.py startapp libraries
```

---

## 4️⃣ 데이터베이스 초기화

```bash
py manage.py makemigrations
py manage.py migrate
```

---

## 5️⃣ 서버 실행

```bash
py manage.py runserver
```

---

## 6️⃣ Django Shell 활용

```bash
# 기본 shell
py manage.py shell

# shell 실행 시 자동 import 내역 출력 (Verbose 모드)
py manage.py shell -v 2

# (추천) ipython 설치 후 사용하면 자동완성, 컬러 출력 지원
pip install ipython
py manage.py shell
```

---

## 7️⃣ 관리자 계정 생성

```bash
py manage.py createsuperuser
```

---

# 🚀 주요 케이스별 요약

### 📌 새 프로젝트 처음 시작할 때

```bash
py -m venv venv
source venv/Scripts/activate
pip install django ipython
pip freeze > requirements.txt
django-admin startproject library_management .
py manage.py startapp libraries
py manage.py makemigrations
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
```

---

### 📌 기존 프로젝트 클론 후 실행할 때

```bash
py -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```

---

### 📌 DB / ORM 실험할 때

```bash
py manage.py shell   # 또는 ipython 설치 후 사용
# 모델 import 후 ORM 코드 실행
```

