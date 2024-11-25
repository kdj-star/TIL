# fileupload/forms.py
from django.forms import ModelForm
from .models import FileUpload
from django.forms import ModelForm, TextInput, EmailInput, NumberInput,FileInput

class FileUploadForm(ModelForm):
    class Meta:
        model = FileUpload
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