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
    
    return render(request, 'articles/index.html')

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
  if request.method == 'POST':
      # fields = ["username", "password1", "password2", "email", 'first_name', 'last_name',"profile_image"]
      
      
      username = request.POST.get('username')
      password1 = request.POST.get('password1')
      password2 = request.POST.get('password2')    
    
      if password1 == password2:
        print('됬음')
      else :
        print('안됬다')
        return redirect('accounts:signup')
    
      email = request.POST.get('email')
      first_name = request.POST.get('first_name')
      last_name = request.POST.get('last_name')
        
      # os.mkdir("../media/userfiles/"+username)
      print('type : ',type(request.FILES['image'].file),'value : ',request.FILES['image'].file)
      print('type : ',type(request.FILES['image'].field_name),'value : ',request.FILES['image'].field_name)
      print('type : ',type(request.FILES['image'].name),'value : ',request.FILES['image'].name)
      print('type : ',type(request.FILES['image'].content_type),'value : ',request.FILES['image'].content_type)
      print('type : ',type(request.FILES['image'].size),'value : ',request.FILES['image'].size)
      print('type : ',type(request.FILES['image'].charset),'value : ',request.FILES['image'].charset)
  
      src = '../image/profile_image/'
      print(src)
      dir = "../media/userfiles/"+username+'/'
      print(dir)
      # shutil.move(src + filename, dir + filename)
      
      
      
      # auth_login(request, user=sign)
      return redirect('accounts:index')
  else:
    sign_form = UserForm()

  context = {
    'sign_form' : sign_form,
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
def edit_profile(request,username):
    user = get_user_model().objects.get(username=username)

    if request.user == user:

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
    else:
      return render(request,'accounts/index.html')
    
    
    
@csrf_exempt
def find_password(request,stage):

  # f = open("D:/FindPassowordInfo.txt", 'r')
  
  

  # code = f.readline()
  # user = f.readline()

  # print(code,user)
  
  # f.close()
  
  # f =open("D:/FindPassowordInfo.txt", 'w')
  # code = '1\n'
  # user = '1\n'
  # f.write(code)
  # f.write(user)
  

  code ='인증메세지'
  
  s = smtplib.SMTP('smtp.gmail.com', 587)
      # TLS 보안 시작
  s.starttls()
  # 로그인 인증()
  
  s.login('TravelMasterSTMP2022', 'wlyhmeupkotqyedv')
  # 보낼 메시지 설정
  
  msg = MIMEText('인증 코드 : '+ code )
  msg['Subject'] = '메일 인증 메시지'
  
  # 메일 보내기

  s.sendmail("TravelMasterSTMP2022@gmail.com",'rkaehdwo@gmail.com' , msg.as_string())
  
  # 세션 종료
  s.quit()

  return render(request,'accounts/find_password.html')
  
  

  # if step == 1:

  #   context = {

  #     'step': 1,

  #   }

  #   return render(request,'accounts/find_password.html',context)
  
  # elif step == 2 :

  #   if request.method == 'POST':
      
  #     email = request.POST['email']
      
  #     print('email : ' + email )

  #     password_user = get_user_model().objects.get(email = email)

  #     # 세션 생성
  #     s = smtplib.SMTP('smtp.gmail.com', 587)
  #     # TLS 보안 시작
  #     s.starttls()
  #     # 로그인 인증()
      
  #     s.login('TravelMasterSTMP2022', 'plqkcjzguzvxkqqn')
  #     # 보낼 메시지 설정
      
      
  #     code = str(10000000 + randint(1,89999999))

  #     msg = MIMEText('인증 코드 : '+ code )
  #     msg['Subject'] = '여행 석사 메일 인증 메시지'
      
  #     # 메일 보내기
  #     if request.POST['email']:
  #       s.sendmail("TravelMasterSTMP2022@gmail.com", request.POST['email'] , msg.as_string())
      
  #     # 세션 종료
  #     s.quit()

  #   context = {

  #     'step': 2,

  #   }

  #   return render(request,'accounts/find_password.html',context)


  # elif step == 3  :
  #   _code= request.POST['code']     

  #   if _code == code :
  #     print('됬다. 인증 성공!')
  #     redirect('accounts:find_password',4)      
  #   else :
  #     context = {

  #     'step': 2,

  #     }

  #     return render(request,'accounts/find_password.html',context) 
      

  #   context = {

  #     'step': 3,

  #   }

  #   return render(request,'accounts/find_password.html',context)


  # elif step == 4 :

  #   if request.POST['password1'] == request.POST['password2']:
  #     password_user.set_password(request.POST['password1'])
  #     password_user.save()
  #     print('비밀번호 변경 가능')
  #     return redirect('accounts:login')
  #   else :
  #     print('비밀번호 변경 불가')

  #     context = {

  #     'step': 2,

  #     }

  #     return render(request,'accounts/find_password.html',context)