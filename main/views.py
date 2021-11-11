from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout as logout_fn

import requests

# Create your views here.
def index(request):
    return redirect('/dashboard')

def login(request):
    return render(request, 'main/login.html')

def logout(request):
    logout_fn(request)
    return redirect('/auth/login')

def dashboard(request):
    return render(request, 'main/index.html')

def pg_dashboard(request):
    return render(request, 'main/index.html')

def rs_dashboard(request):
    return render(request, 'main/index.html')

def test_api(request):
    response = requests.get('https://script.google.com/macros/s/AKfycbxbZj_rtEqCS7ARCwlx3-7Uk8IfQGtw97VWhGjXB1R9QnIJqBaE-uODJ24dIRje9yE/exec?sheetName=Filtered Data')
    print(response.json())
    return HttpResponse('API Tested')
