from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('api/', views.home),
    path('token/', obtain_auth_token, name='obtain-token')
]
