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
        print(user, 'Hi')
        if user is not None:
            login_fn(request, user)
            # if user.role == 'hc-member':
            #     return redirect('main:invitees')
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
        if user.is_superuser:
            pass
        elif (user.role == 'warden') or (user.role == 'hc-member'):
            index = header.index('hall of residence (as recorded in erp)')
            body = [item for item in body if item[index]==user.hall]
        elif user.role == 'hod':
            index = header.index('department')
            body = [item for item in body if item[index]==user.department]
        else:
            return HttpResponse('Not authorized to access this route')
        print()
        # filter based on hall or dep based on the role
        return render(request, 'main/index.html', {
            'user': user,
            'table_header': header,
            'table_body': body,
            'dashboard_title': 'UG Campus Residents'
        })

def pg_dashboard(request):
    user = request.user
    if not user.is_authenticated:
        print(user)
        return redirect('main:login')
    else:
        response = requests.get(config('API_ENDPOINT') + '?sheetName=PG')
        data = response.json()['data']
        header = data['header']
        body = data['data']
        if user.is_superuser:
            pass
        elif (user.role == 'warden') or (user.role == 'hc-member'):
            index = header.index('hall of residence (as recorded in erp)')
            body = [item for item in body if item[index]==user.hall]
        elif user.role == 'hod':
            index = header.index('department')
            body = [item for item in body if item[index]==user.department]
        else:
            return HttpResponse('Not authorized to access this route')
        print()
        # filter based on hall or dep based on the role
        return render(request, 'main/index.html', {
            'user': user,
            'table_header': header,
            'table_body': body,
            'dashboard_title': 'PG Campus Residents'
        })

def rs_dashboard(request):
    user = request.user
    if not user.is_authenticated:
        print(user)
        return redirect('main:login')
    else:
        response = requests.get(config('API_ENDPOINT') + '?sheetName=RS')
        data = response.json()['data']
        header = data['header']
        body = data['data']
        if user.is_superuser:
            pass
        elif (user.role == 'warden') or (user.role == 'hc-member'):
            index = header.index('hall of residence (as recorded in erp)')
            body = [item for item in body if item[index]==user.hall]
        elif user.role == 'hod':
            index = header.index('department')
            body = [item for item in body if item[index]==user.department]
        else:
            return HttpResponse('Not authorized to access this route')
        print()
        # filter based on hall or dep based on the role
        return render(request, 'main/index.html', {
            'user': user,
            'table_header': header,
            'table_body': body,
            'dashboard_title': 'RS Campus Residents'
        })

def invitee_dashboard(request):
    user = request.user
    if not user.is_authenticated:
        print(user)
        return redirect('main:login')
    else:
        response = requests.get(config('API_ENDPOINT') + '?sheetName=Invitees')
        data = response.json()['data']
        header = data['header']
        body = data['data']
        if user.is_superuser:
            pass
        elif user.role == 'hc-member':
            index = header.index('hall of residence (as recorded in erp)')
            body = [item for item in body if item[index]==user.hall]
        else:
            return HttpResponse('Not authorised to view this page')
        print()
        # filter based on hall or dep based on the role
        return render(request, 'main/index.html', {
            'user': user,
            'table_header': header,
            'table_body': body,
            'dashboard_title': 'Campus Invitees Dashboard'
        })

def test_api(request):
    response = requests.get(config('API_ENDPOINT') + '?sheetName=UG')
    print(response.json()['data'])
    return HttpResponse('API Tested')
