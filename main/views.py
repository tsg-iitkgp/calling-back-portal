from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as login_fn, logout as logout_fn

import requests

# Create your views here.
def index(request):
    return redirect('/dashboard')

def login(request):
    if request.user.is_authenticated:
        return redirect('main:dashboard')
    if(request.method=='POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login_fn(request, user)
            return redirect('main:dashboard')
        else:
            return render(request, 'main/login.html')
    else:
        return render(request, 'main/login.html')

def logout(request):
    logout_fn(request)
    return redirect('main:login')

def dashboard(request):
    user = request.user
    if not user.is_authenticated:
        print(user)
        return redirect('main:login')
    else:
        return render(request, 'main/index.html', {
            user: user,
        })

def pg_dashboard(request):
    return render(request, 'main/index.html')

def rs_dashboard(request):
    return render(request, 'main/index.html')

def test_api(request):
    response = requests.get('https://script.google.com/macros/s/AKfycbxbZj_rtEqCS7ARCwlx3-7Uk8IfQGtw97VWhGjXB1R9QnIJqBaE-uODJ24dIRje9yE/exec?sheetName=Filtered Data')
    print(response.json())
    return HttpResponse('API Tested')
