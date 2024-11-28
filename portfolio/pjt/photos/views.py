from django.shortcuts import render ,redirect
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from .forms import PhotoUploadForm,CommentForm
from .models import photo,comment

# Create your views here.

import random


def index(request):
    images = photo.objects.all() 



    context = {
            'A': 'A',
            'images' : images
    }

    return render(request, 'photos/index.html', context)

def second_index(request):
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



def detail(request,pk):

    _photo =photo.objects.get(id=pk)

    comments = comment.objects.filter(photo=_photo)
    comment_form = CommentForm()
            
    context={
        
        'photo':_photo,
        'comment_form':comment_form,
        'comments' : comments,


    }



    return render(request,'photos/detail.html',context)

def comments_create(request, pk):
    if request.user.is_authenticated:
        _photo = photo.objects.get(id=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            _comment = comment_form.save(commit=False)
            _comment.photo = _photo
            _comment.user = request.user
            _comment.save()
        return redirect('photos:detail', pk)
    return redirect('accounts:login')



def comments_delete(request, photo_pk, comment_pk):
    if request.user.is_authenticated:
        _comment = comment.objects.get(id = comment_pk)
        if request.user == _comment.user:
            _comment.delete()
    return redirect('photos:detail', photo_pk)


