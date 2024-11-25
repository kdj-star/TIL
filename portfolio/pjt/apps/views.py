from django.shortcuts import render ,redirect
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

import random


def index(request):
    

    return render(request,'apps/index.html')

def lotto(request):
    

    return render(request,'apps/lotto.html')

def practice(request):
    
    send_test_email()

    return render(request,'apps/practice.html')

def image_practice(request):

    return render(request,'apps/image_practice.html')


@csrf_exempt
def email_authentication(request):

    if request.method == 'POST':
        email = request.POST.get('email')

        tmp = str(random.randint(0,1000000))

        code = tmp

        for i in range(0,6-len(tmp)):
            code = '0' + code
        
        send_mail(
        '이메일 인증',
        code,
        'rkaehdwo@gmail.com ',
        [email],
        fail_silently=False,
        )


        context = {

            'email': email ,
            'code' : code,

        }

        return render(request,'apps/code.html',context)    


    return render(request,'apps/email_authentication.html')

def send_test_email():
    send_mail(
        '제목',
        '본문 내용',
        'rkaehdwo@gmail.com ',
        ['kdj1994@kakao.com'],
        fail_silently=False,
    )


from .forms import FileUploadForm
from .models import FileUpload

def fileUpload(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        img = request.FILES["imgfile"]
        fileupload = FileUpload(
            title=title,
            content=content,
            imgfile=img,
        )
        fileupload.save()
        return redirect('apps:fileupload')
    else:
        fileuploadForm = FileUploadForm
        context = {
            'fileuploadForm': fileuploadForm,
        }
        return render(request, 'apps/fileupload.html', context)