from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer

# Create your views here.
def article_list_html(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/article_list.html', context)

def json_01(request):
    articles = Article.objects.all()
    json_articles = []

    for article in articles:
        json_articles.append(
            {
            'title': article.title,
            'content': article.content,
            'created_at': article.created_at,
            'updated_at': article.updated_at,
            }
        )

    return JsonResponse(json_articles, safe=False)

def json_02(request):
    articles = Article.objects.all()
    res_data = serializers.serialize('json', articles)
    return HttpResponse(res_data, content_type="application/json")


@api_view(['GET'])
def json_drf(request):
    articles = Article.objects.all()
    serializers = ArticleSerializer(articles, many=True)
    return Response(serializers.data)