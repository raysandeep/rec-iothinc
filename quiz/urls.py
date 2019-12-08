from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
   path('login/',views.user_login,name='login'),
   path('logout/',views.user_logout,name='logout'),
   path('register/',views.register,name='register'),
   path('dash/',views.dash,name='dash'),
   path('admin',views.user_admin_register)

]
