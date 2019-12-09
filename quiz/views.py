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
from .models import SN,QN,Questions
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import SNSerializer
from quizapp.views import home
from django.http import HttpResponse 


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
            return redirect('/login')
        return redirect('/')
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
            request.session['register']=reg
            messages.success(request, 'Succesfully Verified OTP! Click on quiz to give quiz', extra_tags='alert')
            return render(request,'dashboard.html')
        else:
            messages.success(request, 'Wrong OTP!!!!', extra_tags='alert')
            return render(request,'dashboard.html')

    else:
        return render(request,'dashboard.html')
def quiz(request):
    if request.method == 'POST':
        print('ans',request.POST.get('ans1'))
        return redirect('quiz/',)
    else:
           
        return render(request,'quizpage.html')


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
            return redirect('/')
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
            return redirect('/')
    else:
        return render(request , 'index.html')

def shome(request):
    choices = Questions.CAT_CHOICES
    print(choices)
    return render(request,
        'quiz/home.html',
        {'choices':choices})

def questions(request , choice):
    if request.method == "GET":
        print(choice)
        ques = Questions.objects.filter(catagory__exact = choice)
        return render(request,
            'quiz/questions.html',
            {'ques':ques})

def result(request):
    print("result page")
    if request.method == 'POST':
        data = request.POST
        datas = dict(data)
        qid = []
        qans = []
        ans = []
        score = 0
        for key in datas:
            try:
                qid.append(int(key))
                qans.append(datas[key][0])
            except:
                print("Csrf")
        for q in qid:
            ans.append((Questions.objects.get(id = q)).answer)
        total = len(ans)
        for i in range(total):
            if ans[i] == qans[i]:
                score += 1
        # print(qid)
        # print(qans)
        # print(ans)
        print(score)
        eff = (score/total)*100
    return render(request,'quiz/result.html',{'score':score,'eff':eff,'total':total})