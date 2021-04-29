from django.db import models

class PatModel(models.Model):
    patientname=models.CharField(max_length=150)
    sex=models.CharField(max_length=1)
    dob=models.DateField()
    phone=models.IntegerField()
    email=models.CharField(max_length=150)
    address=models.CharField(max_length=350)
    disease=models.CharField(max_length=150)
    doctor=models.CharField(max_length=150)
    drug=models.CharField(max_length=150)
    drugstrength=models.CharField(max_length=150)
    drugduration=models.CharField(max_length=150)
    prescriptionadvice=models.CharField(max_length=150)
    remarks=models.CharField(max_length=150)

