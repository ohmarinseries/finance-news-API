from django.urls import path
from . import views

symbols_list = views.SymbolViewSet.as_view({
    'post': 'create'
})

articles_list = views.ArticleViewSet.as_view({
    'get': 'list'
})

urlpatterns = [
    path('articles/<int:id>/', articles_list),
    path('symbols/', symbols_list),
]