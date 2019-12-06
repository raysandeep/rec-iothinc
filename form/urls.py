from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from .models import Snippet
from .serializers import SnippetSerializer

urlpatterns = [
    path('api/', views.home),
    path('token/', obtain_auth_token, name='obtain-token'),
    url('filter/',views.FilterList.as_view(queryset=Snippet.objects.all(), serializer_class=SnippetSerializer))
]
