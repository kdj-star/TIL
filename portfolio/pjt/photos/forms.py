# fileupload/forms.py
from django.forms import ModelForm
from .models import photo,comment
from django.forms import ModelForm, TextInput, EmailInput, NumberInput,FileInput

class PhotoUploadForm(ModelForm):
    class Meta:
        model = photo
        fields = ['title', 'imgfile', 'content']

        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 300px;',
                'placeholder': 'title'

                }),
            'imgfile': FileInput(attrs={
                'class': "form-control",
                'style': 'width: 300px;',
                'id':'image-file',
                 'onchange': "readURL(this);"
                }),
            'content': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 300px; height:100px;',
                'placeholder': 'content',
            }),

        }

class CommentForm(ModelForm):

    class Meta:
        model = comment
        # fields = '__all__'
        exclude = ('photo', 'user',)

        widgets = {
            'content': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 780px; height:200px; margin-bottom:10px;',
                'placeholder': 'content'

                }),
            

        }