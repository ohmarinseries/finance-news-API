from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import Article, Symbols
from .serializer import ArticleSerializer, ArticleViewSerializer, SymbolSerializer


class ArticleViewSet(viewsets.ViewSet):
    def list(self, request, id):
        serializer = ArticleViewSerializer(Article.objects.filter(symbol=id), many=True)

        return Response(serializer.data, status.HTTP_200_OK)


class SymbolViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = SymbolSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.validated_data, status.HTTP_201_CREATED)

