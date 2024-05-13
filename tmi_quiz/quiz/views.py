from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Person
from django.views.decorators.csrf import csrf_exempt

from urllib import response
from django.http import HttpResponse
import json

# Create your views here.
def index(request):
    return render(request, 'index.html')

def question(request, question_id):
    ongoing = Person.objects.get(name = request.user)
    return render(request, 'q{0}.html'.format(question_id), {'ongoing': ongoing})

def comment(request):
    if request.method == 'POST':
        #print(request.user, '########')
        ongoing_user = Person.objects.filter(name = request.user).update(
            comment = request.POST['comment']
        )
        return redirect("scoring")

    return render(request, 'comment.html')


def login(request):
    found_user = User.objects.filter(username = request.POST.get('username'))

    if len(found_user) > 0 :
            error = '이미 존재하는 닉네임입니다.'
            return render(request, 'nickname.html', {'error':error})

    ## 유저 회원가입 후 로그인 처리
    if request.method == 'POST':
        new_user = User.objects.create_user(
            username = request.POST['username'],
        )
        auth.login(
            request,
            new_user,
            backend='django.contrib.auth.backends.ModelBackend'
        )
        print(new_user)
    
        Person.objects.create(
            user = new_user,
            name = request.POST['username']
        )
        return redirect("tutorial")

    return render(request, 'nickname.html')

def tutorial(request):
    return render(request, 'tutorial.html')

def scoring(request):
    return render(request, 'scoring.html')

def result(request):
    ongoing_user = Person.objects.get(name = request.user)
    print(ongoing_user)
    return render(request, 'result.html', {"score": ongoing_user.score})

@csrf_exempt
def answer(request):
    request_body = json.loads(request.body)
    
    

    print(request_body['score'],'******')
    ongoing_user = Person.objects.filter(name = request.user).update(
            score = request_body['score']
        )
    return HttpResponse({'signal': 'great'})