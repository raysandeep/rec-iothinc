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
import requests
import pyqrcode
from PIL import Image
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import png
from .models import SN
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import SNSerializer


# Create your views here.
def user_login(request):
    if request.method == "POST":
        username = request.POST['name']
        password =  request.POST['password']
        request.session['username'] = username
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
        return render(request, 'login1.html')

def user_admin_register(request):
    if request.method == "POST":
        username = request.POST['name']
        email = request.POST['email'] 
        password =  request.POST['password']
        
        
        user = User.objects.create_superuser(username = username ,email=email, password=password)
        print(user.save())
        messages.info(request, "Succesfully Registered")
        return redirect('/login')
    else:
        return render(request, 'alogin.html')



def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('/login')
def boola(word):
    print("wrod",word)
    if word=="on":
        return True
    else:
        return False




def dash(request):
    if request.method == "POST":
        reg = request.POST['regno']
        otp = request.POST['otp']
        data = SN.objects.filter(register_number = reg)
        for i in data:
            print(i.register_number)
            c_otp = i.otp
        if c_otp == otp:
            if request.method == 'POST':
                questions=[]
                oo1=[]
                oo2=[]
                oo3=[]
                oo4=[]
                c0=[]
                for i in range(3):
                    data = SN.objects.filter(q_id = i+1)
                    for i in data:
                        questions.append(i.question)
                        oo1.append(i.o1)
                        oo2.append(i.o2)
                        oo3.append(i.o3)
                        oo4.append(i.o4)
                        c0.append(i.co)
                print(data)
                return render(request,'quizpage.html',{'reg':reg,'qns':questions,'o1':oo1,'o2':oo2,'o3':oo3,'o4':oo4})
        else:
            messages.success(request, 'Wrong OTP!!!!', extra_tags='alert')
            return render(request,'dashboard.html')

    else:
        return render(request,'dashboard.html')
def quiz(request):
    if request.method == 'POST':
        questions=[]
        oo1=[]
        oo2=[]
        oo3=[]
        oo4=[]
        c0=[]
        for i in range(3):
            data = SN.objects.filter(q_id = i+1)
            for i in data:
                questions.append(i.question)
                oo1.append(i.o1)
                oo2.append(i.o2)
                oo3.append(i.o3)
                oo4.append(i.o4)
                c0.append(i.co)
        print(data)
        return render(request,'quizpage.html',{'reg':reg,'qns':questions,'o1':oo1,'o2':oo2,'o3':oo3,'o4':oo4,'co':c0})


@csrf_exempt
def api(request):
    if request.method == 'GET':
        snippets = SN.objects.all()
        serializer = SNSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)    





@login_required(login_url='/login')
def register(request):
    if request.method == "POST":
        print(request.POST.get('Technical'))
        full_name = request.POST['name']
        email = request.POST['email']
        regis_number = request.POST['register']
        phone =  request.POST['phone']
        Technical =  boola(request.POST.get('Technical'))
        Management =  boola(request.POST.get('Management'))
        Design =  boola(request.POST.get('Design'))
        

        if User.objects.filter(email = email).exists():
            messages.info(request , "Email Already exist")
            return redirect('register/')
        elif User.objects.filter(username = phone).exists():
            messages.info(request , "Phone NUmber Already Exisits")
            return redirect('register/')
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
            #msg.send()
            messages.info(request , "Succesfully Registered!!")
            return redirect('/quiz/dash')
    else:
        return render(request , 'index.html')
