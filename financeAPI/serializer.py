from rest_framework import serializers
from .models import Article, Symbols


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class ArticleViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        depth = 1


class SymbolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symbols
        fields = '__all__'


