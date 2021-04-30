from django import  forms
from HealthcareCRUD.models import PatModel

class Patforms(forms.ModelForm):
    class Meta:
        model=PatModel
        fields="__all__"