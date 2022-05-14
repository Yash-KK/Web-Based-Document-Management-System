from dataclasses import fields
from django import forms
from .models import File_Upload


class UploadFile_Form(forms.ModelForm):
    class Meta:
        model = File_Upload
        fields = ["file_name","my_file"]
        