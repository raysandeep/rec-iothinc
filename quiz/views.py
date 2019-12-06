from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import os
from django.shortcuts import render,redirect
import re
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def user_login(request):
    if request.method == "POST":

        username = request.POST['username']
        password =  request.POST['password']
        request.session['user'] = username

        print(password)
        user = auth.authenticate(username=username,password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            print("LOGIN SUCCESS")
            redirect('/')
        else:
            messages.info(request, "Wrong Credentials")
            return redirect('login')
        return redirect('/dash')
    else:
        return render(request, 'index.html')

'''
def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('/login')


@login_required(login_url='/login/')
def register(request):
    if request.method == "POST":
        first_name = request.POST['fname']
        email = request.POST['email']

        phone_number = request.POST['lname']
        password =  request.POST['password']
        confirm_password =  request.POST['cpassword']
        
        if password == confirm_password:
            if User.objects.filter(email = email).exists():
                messages.info(request , "Email Already exist")
                return redirect('/login')
            elif User.objects.filter(username = phone_number).exists():
                messages.info(request , "Phone NUmber Already Exisits")
                return redirect('/login')
            else:
                user = User.objects.create_user(first_name = first_name, last_name=phone_number,username=email, password=password) #change model name
                user.save()
                redirect('/login')
        else:
            messages.info(request, "Password Not Matching")
            redirect('register')
        return redirect('/login')
    else:
        return render(request , 'register.html')





'''