from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),                     # 전체 목록
    path('<int:pk>/', views.detail, name='detail'),           # 상세 조회
    path('new/', views.new, name='new'),                      # 글 작성 폼
    path('create/', views.create, name='create'),             # 글 생성
    path('<int:pk>/delete/', views.delete, name='delete'),    # 글 삭제
    path('<int:pk>/edit/', views.edit, name='edit'),          # 글 수정 폼
    path('<int:pk>/update/', views.update, name='update'),    # 글 수정 반영
]
