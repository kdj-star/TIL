from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserForm
from .forms import CustomUserChangeForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

from django.http import HttpResponse
import os
from photos.models import photo
import smtplib
from email.mime.text import MIMEText
import shutil


# Create your views here.

def index(request):
    
    
    return render(request,'accounts/index.html')


def find_password(request,stage):
    
    print(stage)
    
    return render(request,'accounts/find_password.html')

@csrf_exempt
def login(request):
  
  if request.user.is_authenticated:
    
    return redirect('accounts:index')

  else:

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:login') 
    
@csrf_exempt
def signup(request):
  
    if  request.user.is_authenticated:
       return redirect('accounts:index')
    else:
        if request.method == 'POST':
            
            form = UserForm(request.POST)
            # 유효성 검사
            if form.is_valid():
                user = form.save()
                # 회원가입 후 로그인 상태로 만들어줌
                return redirect('accounts:login')
        else:
            form = UserForm()

        context = {
            'form' : form,
        }
        
        return render(request, 'accounts/signup.html', context)

def user_list(request):
    
    users = get_user_model().objects.all()
    
    context ={
        
        'users' : users,
        
    }
    
    return render(request,'accounts/user_list.html',context)

def delete(request,pk): 
    
  user = get_user_model().objects.get(pk=pk).delete()

  return redirect('accounts:user_list')

  
def profile(request,username):
  
    User =  get_user_model().objects.get(username = username)
    
    context ={
      
      'User': User,
          
    }
    
    return render(request,'accounts/profile.html',context)
        
  

@login_required
def edit_profile(request):

      if request.method == 'POST':
          form = CustomUserChangeForm(request.POST ,instance=request.user)
          if form.is_valid():
              user = form.save()  
              try:
                user.profile_image =request.FILES['image']
                user.save()
              except:
                print('error')


              return redirect('accounts:index')
      else:
          form = CustomUserChangeForm(instance=request.user)
      
      context = {
          'form': form,
      }

      return render(request,'accounts/edit_profile.html',context)




@csrf_exempt

def change_password(request):
    context= {}
    if  request.user.is_authenticated:
        if request.method == "POST":
            current_password = request.POST.get("origin_password")
            user = request.user
            if check_password(current_password,user.password):
                new_password = request.POST.get("password1")
                password_confirm = request.POST.get("password2")
                if new_password == password_confirm:
                    user.set_password(new_password)
                    user.save()
                    return redirect("accounts:index")
                else:
                    context.update({'error':"새로운 비밀번호를 다시 확인해주세요."})
        else:
            context.update({'error':"현재 비밀번호가 일치하지 않습니다."})

        return render(request, "accounts/change_password.html",context)
    else:
        return redirect('accounts:index')
    

def password(request):



    return redirect('accounts:change_password')
    
    
