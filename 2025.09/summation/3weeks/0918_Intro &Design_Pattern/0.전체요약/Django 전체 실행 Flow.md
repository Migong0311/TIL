
# 🛠️ 가상환경 생성 \~ 서버 실행 · 앱 생성 (bash)

## 0) 작업 폴더 진입

```bash
# 작업용 폴더 만들기 및 이동
mkdir -p ~/workspace/django-first && cd ~/workspace/django-first
```

## 1) 가상환경 생성·활성화

```bash
# 가상환경 생성
python -m venv venv

# 활성화 (Windows Git Bash)
source venv/Scripts/activate

# 활성화 (macOS/Linux)
# source venv/bin/activate
```



## 2) pip 업데이트 및 Django 설치

```bash
# Django 설치
pip install django

# 설치 확인
python -m django --version
which python
which pip
```

## 3) 프로젝트 생성

```bash
# 현재 폴더에 프로젝트 생성 (마침표 중요)
django-admin startproject firstpjt .

# django-admin이 인식 안 되면 아래 대체 명령 사용
# python -m django startproject firstpjt .
```

## 4) 앱 생성

```bash
# 예: articles 앱 생성
python manage.py startapp articles
```

> 생성 후 `firstpjt/settings.py` 의 `INSTALLED_APPS` 에 앱 이름 추가:

```python
INSTALLED_APPS = [
    'articles',   # ← 추가
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

## 5) (선택) 템플릿 폴더와 기본 파일 만들기

```bash
# Django가 기본 인식하는 구조로 템플릿 디렉터리 생성
mkdir -p articles/templates/articles

# 기본 템플릿 파일 생성
cat > articles/templates/articles/index.html << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>Document</title></head>
<body><h1>Hello, Django!</h1></body>
</html>
EOF
```

## 6) (선택) URL · View 최소 구성

```bash
# urls.py에 경로 추가 (편집기에서 직접 수정)
# from articles import views
# urlpatterns = [ path('admin/', admin.site.urls), path('articles/', views.index), ]

# views.py에 기본 뷰 추가
cat > articles/views.py << 'EOF'
from django.shortcuts import render

def index(request):
    return render(request, 'articles/index.html')
EOF
```

## 7) 마이그레이션 및 서버 실행

```bash
# 기본 DB 테이블 생성
python manage.py migrate

# 개발 서버 실행
python manage.py runserver
```

## 8) 접속

```
http://127.0.0.1:8000/articles/
```

---

### 참고

* 가상환경 비활성화

```bash
deactivate
```

* Git에 올릴 때는 `venv/` 폴더를 `.gitignore` 에 추가하고 **requirements.txt** 로 의존성 공유 권장

```bash
pip freeze > requirements.txt
# 다른 환경에서 재현
# pip install -r requirements.txt
```
