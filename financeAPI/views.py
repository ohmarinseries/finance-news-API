from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination
from .models import Article, Symbols
from .serializer import ArticleSerializer, ArticleViewSerializer, SymbolSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('symbol_id')
    serializer_class = ArticleViewSerializer
    pagination_class = StandardResultsSetPagination


class SymbolViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = SymbolSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.validated_data, status.HTTP_201_CREATED)

