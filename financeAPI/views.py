from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import ArticleModel
from .serializer import ArticleSerializer



