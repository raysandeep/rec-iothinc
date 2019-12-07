from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
from .models import Snippet
from .serializers import SnippetSerializer

urlpatterns = [
   path('login/',views.home,name='home'),
   url('filter/',views.FilterList.as_view(queryset=Snippet.objects.all(), serializer_class=SnippetSerializer))
]
