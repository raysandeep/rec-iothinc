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
import random
import string 
import pyqrcode
from PIL import Image
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import png
from .models import SN

# Create your views here.
def user_login(request):
    if request.method == "POST":
        username = request.POST['name']
        password =  request.POST['password']
        print(username)
        user = auth.authenticate(username=username,password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            print("LOGIN SUCCESS")
            redirect('/')
        else:
            messages.info(request, "Wrong Credentials")
            return redirect('login')
        return redirect('/login')
    else:
        return render(request, 'login1.html')

def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('/login')
def boola(word):
    if word=="on":
        return True
    else:
        return False


#@login_required(login_url='/login/')
def register(request):
    if request.method == "POST":
        full_name = request.POST['name']
        email = request.POST['email']
        regis_number = request.POST['register']
        phone =  request.POST['phone']
        Technical =  boola(request.POST['Technical'])
        Management =  boola(request.POST['Management'])
        Design =  boola(request.POST['Design'])
        

        if User.objects.filter(email = email).exists():
            messages.info(request , "Email Already exist")
            return redirect('/api')
        elif User.objects.filter(username = phone).exists():
            messages.info(request , "Phone NUmber Already Exisits")
            return redirect('/api')
        else:
            res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 6)) 
            user = SN(name = full_name, email_id=email,register_number=regis_number,phone=phone, tech=Technical,mgt=Management,design=Design,otp=res) #change model name
            user.save()
            url = pyqrcode.create(regis_number)  
            # Create and save the png file naming "myqr.png" 
            url.png('static/'+regis_number+'.png', scale = 8) 
            subject, from_email, to = '[ LOGIN CRED ] IoThinC VIT Recuirtments  ', 'rayanuthalas@gmail.com', email
            text_content = 'This is an important message from IoThinC-VIT. Please use attached QR Code for personal interview. Your OTP fro quiz is '+res
            html_content = '<p>This is an <strong>important</strong> message from <b>IoThinC-VIT.</b> Please use attached QR Code for personal interview. Your OTP fro quiz is <b>'+res+"</b></p>"
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.attach_file('static/'+regis_number+'.png')
            msg.send()
            messages.info(request , "Succesfully Registered!!")
            return redirect('/api')
    else:
        return render(request , 'index.html')
