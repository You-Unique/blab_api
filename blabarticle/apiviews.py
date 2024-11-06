from rest_framework import generics
from blabarticle import serializers
from .models import Article

class ArticleAllViews(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = serializers.ArticleSerializer


class ArticleAllViews(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = serializers.ArticleSerializer