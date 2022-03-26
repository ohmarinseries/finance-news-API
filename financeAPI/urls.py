from django.urls import path
from . import views

symbols_list = views.SymbolViewSet.as_view({
    'post': 'create'
})


urlpatterns = [
    path('articles/', views.ArticleViewSet.as_view({'get': 'list'})),
    path('symbols/', symbols_list),
]