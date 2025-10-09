
## 아래는 금일 과목평가 대비 모음집이므로 금일안에 삭제되는 임시 파일입니다.

# Django 1시간 합격 압축 노트
> [찐막확인용 로직](https://github.com/Migong0311/TIL/tree/september/07-03-django-authentication-system)

## 0) 60분 학습 플랜

* (10분) 프로젝트/가상환경/마이그레이션/런서버 명령어
* (10분) MTV 패턴 + DTL 문법 치트시트
* (20분) CRUD 앱(articles) — `models/forms/urls/views/templates`
* (20분) Auth 앱(accounts) — 로그인/로그아웃/회원가입/수정/비번변경 + 템플릿

---

## 1) 가상환경·프로젝트·마이그레이션·서버

```bash
# 가상환경
python -m venv venv
# Win: venv\Scripts\activate   |  mac/linux: source venv/bin/activate
venv\Scripts\activate

# 설치 & 생성
pip install django
django-admin startproject config .
python manage.py startapp articles
python manage.py startapp accounts

# 앱 등록 (config/settings.py)
# INSTALLED_APPS에 'articles', 'accounts' 추가
# (선택) LOGIN_URL = 'accounts:login'

# DB 준비
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# 서버
python manage.py runserver
```

---

## 2) MTV(디자인 패턴) & 요청 흐름

* **M(Model)**: DB 스키마 + ORM
* **T(Template)**: 화면 렌더(DTL)
* **V(View)**: 요청 처리 로직(데이터 준비 → 템플릿 렌더)

**요청 흐름**: 브라우저 → **URLconf** → **View** → **Model**(CRUD) → **Template** 렌더 → 응답

> 암기: **U-V-M-T** (URL → View → Model → Template)

---

## 3) DTL(장고 템플릿) 치트시트

```html
{{ 변수 }}                       <!-- 출력 -->
{% if user.is_authenticated %} ... {% else %} ... {% endif %}
{% for obj in qs %} {{ forloop.counter }} {% empty %}없음{% endfor %}
<a href="{% url 'app:name' arg %}">링크</a>
<form method="post">{% csrf_token %} ... </form>
{% extends 'base.html' %}  {% block content %}{% endblock %}
{% include 'path/snippet.html' %}
```

---

## 4) CRUD 앱 — articles

### 4-1) `articles/models.py`

```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

### 4-2) `articles/forms.py`

```python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content')
```

### 4-3) `articles/urls.py`

```python
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]
```

### 4-4) `articles/views.py` 

```python
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

def index(request):
    articles = Article.objects.order_by('-id')
    return render(request, 'articles/index.html', {'articles': articles})

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'articles/detail.html', {'article': article})

def create(request):
    form = ArticleForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)
    return render(request, 'articles/form.html', {'form': form, 'mode': 'create'})

def update(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(request.POST or None, instance=article)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('articles:detail', article.pk)
    return render(request, 'articles/form.html', {'form': form, 'mode': 'update'})

def delete(request, pk):
    if request.method == 'POST':
        article = Article.objects.get(pk=pk)
        article.delete()
    return redirect('articles:index')

```

### 4-5) 템플릿

`templates/base.html`

```html
<!doctype html>
<html>
<head><meta charset="utf-8"><title>Django</title></head>
<body>
  <nav>
    <a href="{% url 'articles:index' %}">Articles</a> |
    {% if user.is_authenticated %}
      안녕하세요, {{ user.username }}
      <form action="{% url 'accounts:logout' %}" method="post" style="display:inline;">
        {% csrf_token %}<button>Logout</button>
      </form>
    {% else %}
      <a href="{% url 'accounts:login' %}">Login</a> /
      <a href="{% url 'accounts:signup' %}">Signup</a>
    {% endif %}
  </nav>
  <hr>
  {% block content %}{% endblock %}
</body>
</html>
```

`templates/articles/index.html`

```html
{% extends 'base.html' %}
{% block content %}
<h1>Articles</h1>
<p><a href="{% url 'articles:create' %}">[New]</a></p>
<ul>
  {% for a in articles %}
    <li><a href="{% url 'articles:detail' a.pk %}">{{ a.title }}</a></li>
  {% empty %}
    <li>게시글이 없습니다.</li>
  {% endfor %}
</ul>
{% endblock %}
```

`templates/articles/detail.html`

```html
{% extends 'base.html' %}
{% block content %}
<h2>{{ article.title }}</h2>
<p>{{ article.content }}</p>

<p>
  <a href="{% url 'articles:update' article.pk %}">[Edit]</a>
</p>

<form action="{% url 'articles:delete' article.pk %}" method="post">
  {% csrf_token %}<button>Delete</button>
</form>

<p><a href="{% url 'articles:index' %}">Back</a></p>
{% endblock %}
```

`templates/articles/form.html`

```html
{% extends 'base.html' %}
{% block content %}
<h2>{% if mode == 'create' %}Create{% else %}Update{% endif %}</h2>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Save</button>
</form>
<p><a href="{% url 'articles:index' %}">Cancel</a></p>
{% endblock %}
```

---

## 5) Auth 앱 — accounts

### 5-1) `accounts/forms.py`

```python
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email')

class ProfileForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name')
```

### 5-2) `accounts/urls.py`

```python
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('update/', views.update, name='update'),
    path('password/', views.password, name='password'),
]
```

### 5-3) `accounts/views.py` *(데코레이터 없이, 로직 내 분기)*

```python
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import SignUpForm, ProfileForm

def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        auth_login(request, form.get_user())
        return redirect('articles:index')
    return render(request, 'accounts/login.html', {'form': form})

def logout(request):
    if request.method == 'POST':
        auth_logout(request)
    return redirect('articles:index')

def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    form = SignUpForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('articles:index')
    return render(request, 'accounts/signup.html', {'form': form})

def update(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    form = ProfileForm(request.POST or None, instance=request.user)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('articles:index')
    return render(request, 'accounts/update.html', {'form': form})

def password(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    form = PasswordChangeForm(request.user, request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        update_session_auth_hash(request, user)  # 비번 변경 후 세션 유지
        return redirect('articles:index')
    return render(request, 'accounts/password.html', {'form': form})
```

### 5-4) 템플릿

`templates/accounts/login.html`

```html
{% extends 'base.html' %}
{% block content %}
<h2>Login</h2>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button>Log in</button>
</form>
<p><a href="{% url 'accounts:signup' %}">Sign up</a></p>
{% endblock %}
```

`templates/accounts/signup.html`

```html
{% extends 'base.html' %}
{% block content %}
<h2>Signup</h2>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button>Join</button>
</form>
{% endblock %}
```

`templates/accounts/update.html`

```html
{% extends 'base.html' %}
{% block content %}
<h2>Profile Update</h2>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button>Save</button>
</form>
{% endblock %}
```

`templates/accounts/password.html`

```html
{% extends 'base.html' %}
{% block content %}
<h2>Password Change</h2>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button>Change</button>
</form>
{% endblock %}
```

---

## 6) Model vs Form vs ModelForm — 5초 암기표 (요청 반영)

| 구분            | 핵심 역할            | 위치          | 주요 메서드                         | 핵심 문장             |
| ------------- | ---------------- | ----------- | ------------------------------ | ----------------- |
| **Model**     | DB 구조 정의(테이블)    | `models.py` | `.save()`, `.objects.create()` | **데이터 설계도**       |
| **Form**      | 사용자 입력 검증        | `forms.py`  | `.is_valid()`, `.cleaned_data` | **입력창+검증기**       |
| **ModelForm** | Model 기반 폼 자동 생성 | `forms.py`  | `.is_valid()`, `.save()`       | **Model+Form 합체** |

**간단 예시**

* Model:

  ```python
  class Student(models.Model):
      name = models.CharField(max_length=20)
      age = models.IntegerField()
  ```
* Form(일반):

  ```python
  class ContactForm(forms.Form):
      title = forms.CharField(max_length=50)
      message = forms.CharField(widget=forms.Textarea)
  ```
* ModelForm:

  ```python
  class StudentForm(forms.ModelForm):
      class Meta:
          model = Student
          fields = ('name','age')
  ```

---

## 7) **외우기 좋은 로직 패턴(시험형 압축)**

### 7-1) CRUD 공통 패턴(생성/수정 통일) — **CFU 패턴**

> **C**reate/**F**orm/**U**pdate 를 하나의 흐름으로

```python
form = ArticleForm(request.POST or None, instance=maybe_obj)
if request.method == 'POST' and form.is_valid():
    saved = form.save()
    return redirect('articles:detail', saved.pk if maybe_obj is None else maybe_obj.pk)
return render(request, 'articles/form.html', {'form': form})
```

### 7-2) 안전 조회(헬퍼 없이) — **FF(First or Failover)**

```python
obj = Article.objects.filter(pk=pk).first()
if not obj:
    return redirect('articles:index')
```

### 7-3) 삭제 — **PRG**

```python
if request.method == 'POST':
    Article.objects.filter(pk=pk).first() and Article.objects.filter(pk=pk).delete()
return redirect('articles:index')
```

### 7-4) 로그인 분기(데코레이터 없이)

```python
if not request.user.is_authenticated:
    return redirect('accounts:login')
```

### 7-5) Auth 5단 묶음 — **L-O-S-U-P**

* **L**ogin, **O**ut, **S**ignup, **U**pdate, **P**assword

---

## 8) `get_object_or_404` & 데코레이터 — **초간단 요약(설명만)**

* **`get_object_or_404(Model, pk=pk)`**: 못 찾으면 자동으로 404 응답. (시험에선 “안전한 단건 조회” 키워드)
* **데코레이터**

  * `@login_required`: 비로그인 접근 시 로그인 페이지로 돌림.
  * `@require_POST`: 해당 뷰를 POST 메서드로만 허용.

> 본 노트의 예시 코드에는 **사용하지 않았고**, 로직 내부 분기로 처리했습니다.

---

## 9) 자주 나오는 단답(객관 대비)

* **MTV**: Model-Template-View, URL→View→Model→Template
* **PRG 패턴**: POST 처리 후 redirect로 새로고침 중복 방지
* **`update_session_auth_hash`**: 비번 변경 후 **세션 유지**
* **DTL 필수**: `{% csrf_token %}`, `{% url %}`, `{% if %}`, `{% for %}`
* **Form 검증**: `form = Form(request.POST or None)` + `if request.method=='POST' and form.is_valid(): ...`
* **마이그레이션 순서**: 모델수정 → `makemigrations` → `migrate`

---

## 10) 미니 모의문제 (객관·주관·서술)

### (객관) 다음 중 PRG 설명으로 옳은 것은?

A) GET 후 redirect로 폼 제출을 반복한다
B) POST 후 redirect하여 새로고침 중복 제출을 막는다 ✅
C) POST 후 render로 에러 페이지를 띄운다
D) GET만 사용한다

### (객관) 비밀번호 변경 직후에도 로그인 유지시키는 함수는?

A) `auth_login`  B) `auth_logout`  C) `update_session_auth_hash` ✅  D) `make_password`

### (주관) MTV에서 View의 역할을 15자 내외로 기술하시오.

> **요청을 처리하고 데이터 준비 후 템플릿 렌더**

### (주관) DTL에서 CSRF를 막기 위해 반드시 포함해야 하는 태그는?

> **`{% csrf_token %}`**

### (서술) Django에서 Model, Form, ModelForm의 차이와 관계를 간단히 서술하시오.

> **Model은 DB 구조 정의, Form은 입력 검증, ModelForm은 특정 Model 기반 폼 자동생성으로 검증 후 저장을 쉽게 한다.**

---

## 11) 마지막 체크리스트 (3분)

* [ ] 가상환경/마이그레이션/createsuperuser/런서버 명령어
* [ ] MTV 흐름 & DTL 태그 4종(변수/if/for/url/csrf)
* [ ] CRUD: index/detail/create/update/delete 연결과 **PRG**
* [ ] Auth: L-O-S-U-P 흐름 & 비번 변경 후 세션 유지
* [ ] **데코레이터 없이도** 로그인 분기/POST 분기 로직 구현 가능
* [ ] `get_object_or_404` 의미만 기억(안전 조회) — 예시는 `filter().first()`로 대체

---

# 📚 TIL (Today I Learned)


> [![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&duration=7000&pause=800&color=15F71B&width=435&lines=A+daily+journey+of+learning+and+growth)](https://git.io/typing-svg)

이 레포지토리는 제가 매일 학습한 내용을 기록하는 공간입니다. 작고 사소하더라도 그날 배운 것을 정리함으로써 지식을 체계화하고, 꾸준한 성장을 추구합니다.

---

## ✍️ 작성 규칙

- 하루에 하나 이상의 TIL 작성
- 간결하게 요점 정리 (5~10분 내에 읽을 수 있도록)
- 코드 예제나 참고 링크는 꼭 포함
- 반복되는 내용도 다시 정리 가능 (복습 목적)

---

## 🌱 목표

- 학습한 내용을 확실히 내 것으로 만들기
- 미래의 나에게 참고 자료 제공
- 꾸준함의 힘을 체감하기

---

## 📌 참고하면 좋은 링크

- [TIL 작성 가이드 - jbranchaud/til](https://github.com/jbranchaud/til)
- [마크다운 문법 정리](https://guides.github.com/features/mastering-markdown/)

---
### 유용한 마크다운 문법

> [!NOTE]
> Useful information that users should know, even when skimming content.

> [!TIP]
> Helpful advice for doing things better or more easily.

> [!IMPORTANT]
> Key information users need to know to achieve their goal.

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.

- <ins>**밑줄예시**</ins>
```markdown
> [!NOTE]
> Useful information that users should know, even when skimming content.

> [!TIP]
> Helpful advice for doing things better or more easily.

> [!IMPORTANT]
> Key information users need to know to achieve their goal.

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.

- <ins>**밑줄예시**</ins>
```
#### 함께 공부하는 분들, 피드백은 언제든 환영합니다 🙌

##### © 2025 Migong0311 and SSAFY. All rights reserved.
