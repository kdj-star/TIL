from django.shortcuts import render ,redirect
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
from .forms import PhotoUploadForm,CommentForm,PhotoChangeForm
from .models import photo,comment

# Create your views here.

import random


def index(request):
    images = photo.objects.all()
    ordered_images = photo.objects.all().order_by('-like_users') 



    context = {
            'A': 'A',
            'images' : images,
            'ordered_images' : ordered_images,
    }

    return render(request, 'photos/index.html', context)

def second_index(request):
    images = photo.objects.all() 



    context = {
            'A': 'A',
            'images' : images
    }

    return render(request, 'photos/display_image.html', context)






def PhotoUpload(request):
    
    if request.user.is_authenticated:
        
        if request.method == 'POST':
            title = request.POST['title']
            content = request.POST['content']
            img = request.FILES["imgfile"]

            photos = photo.objects.create(title=title,content=content,imgfile=img,user=request.user)
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





def detail(request,pk):

    _photo =photo.objects.get(id=pk)
    
    comments = comment.objects.filter(photo=_photo)
    comment_form = CommentForm()
    likes =_photo.like_users.all()
            
    context={
        
        'photo':_photo,
        'comment_form':comment_form,
        'comments' : comments,
        'likes':likes,


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

@csrf_exempt
@require_POST
def likes(request, photo_pk):
    if request.user.is_authenticated:
        _photo = photo.objects.get(id=photo_pk)

        if _photo.like_users.filter(pk=request.user.pk).exists():
            _photo.like_users.remove(request.user)
        else:
            _photo.like_users.add(request.user)
        return redirect('photos:index')
    return redirect('accounts:login')


def PhotoUpdate(request,photo_pk):
    
    if request.user:
        
        _photo = photo.objects.get(id=photo_pk)

        if request.method == 'POST':
            _photo.title = request.POST['title']
            _photo.content = request.POST['content']
            _photo.imgfile = request.FILES["imgfile"]
            _photo.save()
            return redirect('photos:index')
        else:
            Form = PhotoChangeForm()
            context = {
                'Form': Form ,
                'photo':photo.objects.get(id=photo_pk),
            }
            return render(request, 'photos/PhotoUpdate.html', context)
    else:
        return redirect('accounts:login')
