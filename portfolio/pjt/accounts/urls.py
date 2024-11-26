from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings


app_name = 'accounts'

urlpatterns = [
    path('', views.index,name='index'),
    path('signup/', views.signup,name='signup'),
    path('login/', views.login,name='login'),
    path('logout/', views.logout,name='logout'),
    path('user_list/',views.user_list,name='user_list'),
    path('delete/<int:pk>', views.delete ,name='delete'),
#    path('<int:user_pk>', views.profile ,name='profile'),
    path('profile/<username>', views.profile ,name='profile'),
    path('edit_profile/<username>', views.edit_profile ,name='edit_profile'), 
    path('find_password/<int:stage>', views.find_password,name='find_password'),
#    path('my_profile/', views.my_profile ,name='my_profile'),
#    path('my_profile/edit/', views.edit_profile ,name='edit_profile'),
] 