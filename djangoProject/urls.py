from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('news/', include('financeAPI.urls')),
    path('admin/', admin.site.urls),
]
