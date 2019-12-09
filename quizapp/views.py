from django.shortcuts import render
from .models import Questions,results
from django.contrib import messages
from django.shortcuts import render,redirect


# Create your views here.
def home(request):
    
    if 'register' not in request.session:
        messages.success(request, 'Please eneter otp', extra_tags='alert')
        return redirect('/')
    else:
        choices = Questions.CAT_CHOICES
        print(choices)
        return render(request,
            'quiz/home.html',
            {'choices':choices})

def questions(request , choice):
    print(choice)
    if request.session['register'] == None:
        messages.success(request, 'Please eneter otp', extra_tags='alert')
        return redirect('/')
    else:
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
        reg =  request.session['register']
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
        del request.session['register']
        results(regis=reg,marks=score)
    return render(request,'quiz/result.html',{'score':"Succefully COmpleted",'reg':reg,})
def about(request):
    return render(request,
        'q/about.html')

def contact(request):
    return render(request,
        'q/contact.html')




#
#
#
#
#
#
#
