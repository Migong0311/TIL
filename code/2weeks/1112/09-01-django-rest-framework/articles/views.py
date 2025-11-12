from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Article
from .serializers import ArticleSerializer,ArticleListSerializer


@api_view(['GET','POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
    


# @api_view(['GET','DELETE','PUT'])
@api_view(['GET','DELETE','PATCH'])
def article_detail(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        seroalizer = ArticleSerializer(article)
        return Response(seroalizer.data)
    elif request.method == 'DELETE':
        pk = article_pk
        title = article.title
        article.delete()
        data = {
            'message' : f'{pk}번 게시글 "{title}"이 삭제되었습니다!'
        }
        return Response(data,status=status.HTTP_200_OK)


    # elif request.method == 'PUT':
    #     serializer = ArticleSerializer(article,data=request.data)
    elif request.method == 'PATCH':
        serializer = ArticleSerializer(article,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    