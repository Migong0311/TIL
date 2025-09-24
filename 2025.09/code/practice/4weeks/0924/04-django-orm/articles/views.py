from django.shortcuts import render
from .models import Article
# Create your views here.
def index(request):
    # 1. DB에 전체 게시글을 조회
    articles = Article.objects.all()

    # 2. 전체 게시글 목록을 템플릿과 함께 응답
    context = {
        'articles': articles
    }
    return render(request,'index.html',context)