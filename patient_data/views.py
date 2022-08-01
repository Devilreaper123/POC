from django.shortcuts import render, redirect
from django.db.models import Q
from .models import PatientData

def details(req):
    patient_data = PatientData.objects.all()
    context = {'patient_data':patient_data}
    return render(req,'patient_data/details.html',context)