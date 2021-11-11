from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout as logout_fn

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
    print()
    return HttpResponse('API Tested')
