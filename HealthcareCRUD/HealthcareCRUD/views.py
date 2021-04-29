from django.shortcuts import render
from HealthcareCRUD.models import PatModel
from django.contrib import messages

def showpat(request):
    showall=PatModel.objects.all()
    return render(request,'Index.html',{"data":showall})

def Insertpat(request):
    if request.method=="POST":
        if request.POST.get('patientname') and request.POST.get('sex') and request.POST.get('dob') and request.POST.get('phone') and request.POST.get('email') and request.POST.get('address') and request.POST.get('disease') and request.POST.get('doctor') and request.POST.get('drug') and request.POST.get('drugstrength') and request.POST.get('drugduration') and request.POST.get('prescriptionadvice') and request.POST.get('remarks'):
            saverecord=PatModel()
            saverecord.patientname=request.POST.get('patientname')
            saverecord.sex=request.POST.get('sex')
            saverecord.dob=request.POST.get('dob')
            saverecord.phone=request.POST.get('phone')
            saverecord.email=request.POST.get('email')
            saverecord.address=request.POST.get('address')
            saverecord.disease=request.POST.get('disease')
            saverecord.doctor=request.POST.get('doctor')
            saverecord.drug=request.POST.get('drug')
            saverecord.drugstrength=request.POST.get('drugstrength')
            saverecord.drugduration=request.POST.get('drugduration')
            saverecord.prescriptionadvice=request.POST.get('prescriptionadvice')
            saverecord.remarks=request.POST.get('remarks')
            saverecord.save()
            messages.success( request,'Patient'+saverecord.patientname+'Details Saved Successfully!')
            return render(request,'Insert.html')
        else:
            return render(request,'Insert.html')
            
