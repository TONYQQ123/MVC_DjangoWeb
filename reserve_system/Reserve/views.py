from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from Reserve.form import CustomForm
from Reserve.models import CustomUser,Rserve
from django.contrib.auth.models import User
import json
from Reserve.custombackend import CustomBackend
from django.contrib import messages
from django.core.cache import cache
import time
import subprocess
import os
from django.conf import settings

#superuser
# name: yu
# email: tony0910242070@gmail.com
# password: 457.....
# Create your views here.
def set_usernameVar(value):
    cache.set('username_var',value)
def get_usernameVar():
    return cache.get('username_var')


def BackHome(request):
    return render(request,'HOME.html')

def Tool(request):
    if request.method == 'POST':
        action=request.POST.get('action')
        if action == 'reservation':
            return reservation(request)
        if action == 'search':
            return detail(request)
        if action == 'logout':
            return Logout(request)
    return render(request,'HOME.html')

def detail(request):
    return redirect('reserve_detail')

def reserve_detail(request):
    if request.method=='POST':
        action=request.POST.get('action')
        if action=='delete':
            return delete_rv(request)
        if action=='update':
            return update_rv(request)
        if action=='query':
            return search(request)
    return render(request,'RvUpdate.html')

def delete_rv(request):
    try:
        id=request.POST.get('id')
        delete_item=Rserve.objects.get(reserve_id=id)
        delete_item.delete()
        messages.success(request,'刪除成功')
        return render(request,'RvUpdate.html')
    except Exception as e:
        messages.success(request,f'刪除失敗 {e}')
        print(e)
        return render(request,'RvUpdate.html')

def update_rv(request):
    try:
        id=request.POST.get('id')
        date=request.POST.get('date')
        need=request.POST.get('need')
        rv=Rserve.objects.get(reserve_id=id)
        rv.date=date
        rv.need=need
        rv.save()
        messages.success(request,'更新成功')
        return render(request,'RvUpdate.html')
    except Exception as e:
        messages.error(request,f'更新失敗 {e}')
        return render(request,'RvUpdate.html')
    
def search(request):
    try:
        id=request.POST.get('id')
        rv=Rserve.objects.get(reserve_id=id)
        date=rv.date
        gender=rv.gender
        detail=rv.need
        rvid=rv.reserve_id
        result = f'預約編號: {rvid}<br>預約日期: {date}<br>性別: {gender}<br>預約事項: {detail}<br>'
        messages.success(request,'查詢成功')
        return render(request, 'RvUpdate.html', {'data': result})
    except Exception as e:
        messages.error(request,f'查詢失敗 {e}')
        return render(request,'RvUpdate.html')

def Logout(request):
    auth.logout(request)
    set_usernameVar('')
    return redirect('index')

def reservation(request):
    return redirect('date')

def generate_rvID(usr_id,date):
    rvID=usr_id[:4]+date[-5:]+str(time.time())[:10]
    print(rvID)
    return rvID
def set_date(request):
    if request.method == 'POST':
        action=request.POST.get('action')
        if action=='submit':
            try:
                user=CustomUser.objects.get(username=get_usernameVar())
            except Exception:
                return render(request,'index.html')
            try:
                date=request.POST.get('date_input')
                gender=request.POST.get('gender')
                details=request.POST.get('details')
                if date is not None and gender is not None:
                    rv=generate_rvID(usr_id=user.user_id,date=date)
                    user.reserves.create(
                        gender=gender,
                        date=date,
                        need=details,
                        reserve_id=rv
                    )
                    messages.success(request,f'預約成功! 預約編號: {rv}')
                    return render(request,'Reservation.html')
                else:
                    messages.error(request,'預約失敗')
                    return render(request,'Reservation.html')
            except Exception as e:
                messages.error(request,f'預約失敗 {e}')
        elif action=='return':
            return redirect('BackHome')
    return render(request,'Reservation.html')
    
        


def login_register(request):
    if request.method == 'POST':
        action=request.POST.get('action')
        if action=='login':
            return login(request)
        if action=='register':
            return register(request)
    return render(request,'index.html')

def login(request):
    # if request.user.is_authenticated:
    #     return HttpResponseRedirect('/h/')
    username=request.POST.get('username','123')
    password=request.POST.get('password','123')
    user=CustomBackend().authenticate(request=request,username=username,password=password)
    if user is not None:
        try:
            auth.login(request,user,backend='Reserve.custombackend.CustomBackend')
            messages.success(request,'登入成功')
            set_usernameVar(username)
            return render(request,'HOME.html',{'user':user})
        except Exception as e:
            messages.error(request,e)
            return render(request,'index.html')
    else:
        messages.error(request,'登入失敗')
        set_usernameVar('')
        return render(request,'index.html')

def register(request):
    form=CustomForm()
    if request.method == 'POST':
        try:
            form=CustomForm(request.POST)
            print(form.is_valid())
            if form.is_valid():
                username=form.cleaned_data['username']
                if CustomUser.objects.filter(username=username).exists():
                    messages.error(request,'註冊失敗')
                    return render(request,'index.html',{'form':form,'error_message':'用戶已存在'})
                NewOne=CustomUser.objects.create_user(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password'],
                    user_id=username+str(time.time())[:10]
                )
                messages.success(request,'註冊成功')
                return redirect('index')
        except Exception as e:
            messages.error(request,e)
            
    contex={'form':form}
    messages.error(request,'註冊失敗')
    return render(request,'index.html',contex)


