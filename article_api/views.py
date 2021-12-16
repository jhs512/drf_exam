from django.http import HttpRequest, HttpResponse, Http404
# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from article_api.models import Article
from article_api.serializers import ArticleSerializer


def index(request: HttpRequest):
    return HttpResponse("안녕")


class ArticleList(APIView):
    def get(self, request: HttpRequest, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request: HttpRequest, format=None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetail(APIView):
    def get_object(self, id: int):
        return get_object_or_404(Article, id=id)

    def get(self, request: HttpRequest, id: int, format=None):
        serializer = ArticleSerializer(self.get_object(id))
        return Response(serializer.data)

    def put(self, request: HttpRequest, id: int, format=None):
        serializer = ArticleSerializer(self.get_object(id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: HttpRequest, id: int, format=None):
        self.get_object(id).delete()
        return HttpResponse(status=204)
