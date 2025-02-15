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

app_name = "apps"


urlpatterns = [
    path('', views.index,name="index"),
    path('count_length/',views.count_length,name='count_length'),
    path('lotto/', views.lotto,name="lotto"),
    path('practice/', views.practice,name="practice"),
    path('email_authentication/',views.email_authentication,name="email_authentication"),
    path('image_practice/', views.image_practice,name="image_practice"),
    path('carousel/',views.carousel,name='carousel'),
    path('drag_and_drop',views.drag_and_drop,name='drag_and_drop'),
    path('sticky_note',views.sticky_note,name='sticky_note'),
    path('create_note',views.create_note,name='create_note'),
    path('update_note/<int:pk>',views.update_note,name='update_note'),
    path('delete_note/<int:pk>',views.delete_note,name='delete_note'),

]
