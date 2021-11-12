from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as login_fn, logout as logout_fn

import requests
from decouple import config

import json

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
        response = requests.get(config('API_ENDPOINT') + '?sheetName=UG')
        data = response.json()['data']
        header = data['header']
        body = data['data']
        print()
        # filter based on hall or dep based on the role
        return render(request, 'main/index.html', {
            'user': user,
            'table_header': header,
            'table_body': body,
            'dashboard': 'UG'
        })

def pg_dashboard(request):
    return render(request, 'main/index.html')

def rs_dashboard(request):
    return render(request, 'main/index.html')

def test_api(request):
    response = requests.get(config('API_ENDPOINT') + '?sheetName=UG')
    print(response.json()['data'])
    return HttpResponse('API Tested')
