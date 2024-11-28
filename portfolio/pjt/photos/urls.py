"""
URL configuration for pjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

app_name = "photos"


urlpatterns = [
    path('', views.index,name="index"),
    path('second_index', views.second_index,name="second_index"),
    path('PhotoUpload/', views.PhotoUpload, name="PhotoUpload"),
    path('display_image/', views.display_image, name="display_image"),
    path('detail/<int:pk>', views.detail ,name='detail'),
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:photo_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
]



