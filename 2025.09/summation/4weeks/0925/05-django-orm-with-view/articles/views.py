from django.shortcuts import redirect, render
from .models import Article

# 메인 페이지: 전체 게시글 조회 (READ - All)
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

# 상세 페이지: 단일 게시글 조회 (READ - one)
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)

# 새 글 작성 폼 (CREATE - FORM)
def new(request):
    return render(request, 'articles/new.html')

# 글 생성 (CREATE)
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article(title=title, content=content)
    article.save()
    return redirect('articles:detail', article.pk)

# 글 삭제 (DELETE)
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

# 글 수정 폼 (UPDATE - form)
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/edit.html', context)

# 글 수정 반영(UPDATE)
def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)
