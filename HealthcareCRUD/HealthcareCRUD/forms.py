from django import forms
from HealthcareCRUD.models import PatModel
from .models import Image


class Patforms(forms.ModelForm):
    class Meta:
        model = PatModel
        fields = "__all__"


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')
