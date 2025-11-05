from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article,Comment
from .forms import ArticleForm, CommentForm


def index(request):
    articles = Article.objects.all()

    context = {
        "articles": articles,
    }
    return render(request, "articles/index.html", context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment = CommentForm()
    comments_content = article.comment_set.all()

    context = {
        "article": article,
        "comment": comment,
        'comments_content' : comments_content, 
    }
    return render(request, "articles/detail.html", context)


def comments(request, pk):
    article = Article.objects.get(pk=pk)
    comment = CommentForm(request.POST)
    if comment.is_valid():
        comment = comment.save(commit=False)  # 댓글을 저장하지 않고 인스턴스만 생성
        comment.article = article  # 댓글에 게시글 정보 추가
        comment.save()  # 댓글 정보 DB에 저장 요청
        return redirect("articles:detail", article.pk)
    return render(
        request,
        "articles/detail.html",
        {
            "article": article,
            "comment": comment,
        },
    )

def comments_delete(request,article_pk,comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail',article_pk)

@login_required
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect("articles:detail", article.pk)
    else:
        form = ArticleForm()
    context = {
        "form": form,
    }
    return render(request, "articles/create.html", context)


@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)

    article.delete()

    return redirect("articles:index")


@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect("articles:detail", article.pk)

    else:
        form = ArticleForm(instance=article)

    context = {
        "article": article,
        "form": form,
    }
    return render(request, "articles/update.html", context)
