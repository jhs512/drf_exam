# Create your views here.
from rest_framework import generics

from article_api.models import Article
from article_api.serializers import ArticleSerializer


class ArticleList3(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetail3(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'id'