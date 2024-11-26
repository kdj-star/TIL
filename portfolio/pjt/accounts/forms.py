from django import forms
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from .models import User
from django.contrib.auth import get_user_model

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email", 'first_name', 'last_name',"profile_image"]
        
        labels = {
        "username" : "아이디", 
        "password1":"비밀번호", 
        "password2":"비밀번호 확인", 
        "email":"이메일", 
        'first_name':"성", 
        'last_name':"이름",
        "profile_image":"프로필 사진",
      }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['username'].help_text = None
    
        

class CustomUserChangeForm(UserChangeForm):
      class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']