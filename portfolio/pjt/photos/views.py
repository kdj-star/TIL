from django.shortcuts import render ,redirect
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

import random


def index(request):
    images = photo.objects.all() 



    context = {
            'A': 'A',
            'images' : images
    }

    return render(request, 'photos/display_image.html', context)

def lotto(request):
    

    return render(request,'photos/lotto.html')

def practice(request):
    
    send_test_email()

    return render(request,'photos/practice.html')

def image_practice(request):

    return render(request,'photos/image_practice.html')


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

        return render(request,'photos/code.html',context)    


    return render(request,'photos/email_authentication.html')

def send_test_email():
    send_mail(
        '제목',
        '본문 내용',
        'rkaehdwo@gmail.com ',
        ['kdj1994@kakao.com'],
        fail_silently=False,
    )


from .forms import PhotoUploadForm
from .models import photo

def PhotoUpload(request):
    
    if request.user.is_authenticated:
        
        if request.method == 'POST':
            title = request.POST['title']
            content = request.POST['content']
            img = request.FILES["imgfile"]
            photos = photo.objects.create(title=title,content=content,imgfile=img)
            photos.save()
            return redirect('photos:index')
        else:
            Form = PhotoUploadForm()
            context = {
                'Form': Form ,
            }
            return render(request, 'photos/PhotoUpload.html', context)
    else:
        return redirect('accounts:login')


    
def display_image(request):

    images = photo.objects.all() 



    context = {
            'A': 'A',
            'images' : images
    }

    return render(request, 'photos/display_image.html', context)

def carousel(request):


    images = photo.objects.all() 

    context = {
            'A': 'A',
            'images' : images
    }
    
    return render(request, 'photos/carousel.html', context)


