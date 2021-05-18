from cdg.models import Proyek
from django.shortcuts import render

def splash(request):
    return render(request, 'splash.html')

def home(request):
    if request.method=='POST':
        proyek=request.POST['proyek']
        Proyek.objects.create(proyek=proyek)

    posts=Proyek.objects.all()
    return render(request,'index.html',{'posts':posts})

def translasi(request):
    return render(request,'translasi.html')

def hasil(request):
    return render(request,'hasil.html')

def database(request):
    return render(request,'database.html')

# crud

def addproyek(request):
    return render(request,'index.html')