from .models import Article, Category
from rest_framework import serializers


class CategorySerializer (serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Category
        fields = ('title',)
        read_only_fields = ('id',)


class ArticleSerializer (serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = "__all__"
        read_only_fields = ("id", 'slug')