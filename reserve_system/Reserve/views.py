from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from Reserve.form import CustomForm
from Reserve.models import CustomUser,Rserve
from django.contrib.auth.models import User
import json
from Reserve.custombackend import CustomBackend
from django.contrib import messages

# Create your views here.
def Tool(request):
    if request.method == 'POST':
        action=request.POST.get('action')
        if action == 'reservation':
            return reservation(request)
        # if action == 'search':
        #     return search(request)
        # if action == 'logout':
        #     return logout
    return render(request,'HOME.html')

def reservation(request):
    return render(request,'Reservation.html')

def set_date(request):
    newone=Rserve()
    if request.method == 'POST':
        action=request.POST.get('action')
        if action=='submit':
            date=request.POST.get('input')
            if date is None:
                date='2023-01-01'
            newone.date=date
            newone.save()
            messages.success(request,'預約成功')
            return render(request,'Reservation.html')
        elif action=='return':
            return render(request,'HOME.html')
    
        


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
    print(username)
    if user is not None:
        auth.login(request,user,backend='Reserve.custombackend.CustomBackend')
        messages.success(request,'登入成功')
        return render(request,'HOME.html',{'user':user})
    else:
        messages.error(request,'登入失敗')
        return render(request,'index.html')

def register(request):
    form=CustomForm()
    if request.method == 'POST':
        form=CustomForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            username=form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                messages.error(request,'註冊失敗')
                return render(request,'index.html',{'form':form,'error_message':'用戶已存在'})
            NewOne=CustomUser(
                username=form.cleaned_data['username']
            )
            NewOne.set_password(form.cleaned_data['password'])
            NewOne.save()
            messages.error(request,'註冊失敗')
            return redirect('index')
    contex={'form':form}
    messages.error(request,'註冊失敗')
    return render(request,'index.html',contex)


