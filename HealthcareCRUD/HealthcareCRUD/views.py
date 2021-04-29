from django.shortcuts import render
from HealthcareCRUD.models import PatModel

def showpat(request):
    showall=PatModel.objects.all()
    return render(request,'Index.html',{"data":showall})