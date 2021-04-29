from django.shortcuts import render,redirect
from HealthcareCRUD.models import PatModel
from django.contrib import messages

def showpat(request):
    showall=PatModel.objects.all()
    return render(request,'Index.html',{"data":showall})

def Insertpat(request):
    
    
    if request.method=="POST":
        print(request)

        # if request.POST.get('patientname') and request.POST.get('sex') and request.POST.get('dob') and request.POST.get('phone') and request.POST.get('email') and request.POST.get('address') and request.POST.get('disease') and request.POST.get('doctor') and request.POST.get('drug') and request.POST.get('drugstrength') and request.POST.get('drugduration') and request.POST.get('prescriptionadvice') and request.POST.get('remarks'):
        
        saverecord=PatModel(
            patientname=request.POST.get('patientname'),
            sex=request.POST.get('sex'),
            dob=request.POST.get('dob'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            address=request.POST.get('address'),
            disease=request.POST.get('disease'),
            doctor=request.POST.get('doctor'),
            drug=request.POST.get('drug'),
            drugstrength=request.POST.get('drugstrength'),
            drugduration=request.POST.get('drugduration'),
            prescriptionadvice=request.POST.get('prescriptionadvice'),
            remarks=request.POST.get('remarks'),
        )
        saverecord.save()
        messages.success(request,'Patient '+request.POST.get('patientname')+' Details Saved Successfully!')
    return render(request,'Insert.html')

def destroy(request, id):  
    obj = PatModel.objects.get(id=id)  
    obj.delete()  
    return redirect("/Index") 

def Editpat(request,id):
    editpatobj = PatModel.objects.get(id=id)  
    return render(request,'Edit.html',{"PatModel":editpatobj})

       
       
            
