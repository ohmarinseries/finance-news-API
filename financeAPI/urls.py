from django.urls import path
from . import views

symbols_list = views.SymbolViewSet.as_view({
    'post': 'create',
    'get': 'list'
})

symbols_details = views.SymbolViewSet.as_view({
    'get': 'retrieve',
    'patch': 'update',
    'delete': 'destroy'
})


urlpatterns = [
    path('articles/', views.ArticleViewSet.as_view({'get': 'list'}), name='article-list'),
    path('symbols/', symbols_list, name='symbol-list'),
    path('symbols/details/<int:id>/', symbols_details, name='symbol-details'),
]