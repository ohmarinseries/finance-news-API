from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination
from .models import Article, Symbols
from .serializer import ArticleSerializer, ArticleViewSerializer, SymbolSerializer
from drf_yasg.utils import swagger_auto_schema


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('symbol_id')
    serializer_class = ArticleViewSerializer
    pagination_class = StandardResultsSetPagination


class SymbolViewSet(viewsets.ViewSet):
    @swagger_auto_schema(request_body=SymbolSerializer)
    def create(self, request):
        serializer = SymbolSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.validated_data, status.HTTP_201_CREATED)

    @swagger_auto_schema(responses={200: SymbolSerializer(many=True)})
    def list(self, request):
        serializer = SymbolSerializer(Symbols.objects.all(), many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    @swagger_auto_schema(responses={200: SymbolSerializer()})
    def retrieve(self, request, id):
        serializer = SymbolSerializer(Symbols.objects.get(pk=id))

        return Response(serializer.data, status.HTTP_200_OK)

    @swagger_auto_schema(request_body=SymbolSerializer)
    def update(self, request, id):
        serializer = SymbolSerializer(instance=get_object_or_404(Symbols, pk=id), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.validated_data, status.HTTP_200_OK)

    def destroy(self, request, id):
        get_object_or_404(Symbols, pk=id).delete()

        return Response("Symbol is deleted", status.HTTP_200_OK)
