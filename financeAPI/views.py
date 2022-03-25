from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import ArticleModel
from .serializer import ArticleSerializer


class ArticleViewSet(viewsets.ViewSet):
    def list(self, request, sym):
        serializer = ArticleSerializer(data=ArticleModel.objects.filter(symbol=sym), many=True)

        return Response(serializer, status.HTTP_200_OK)

    def test_celery(self, request):
        pass



