from cdg.models import Proyek
from projekppl.forms import ProyekForm 
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def splash(request):
    return render(request, 'splash.html')

def home(request):   
    posts=Proyek.objects.all()
    return render(request,'index.html',{'posts':posts})

def tambah_proyek(request):  
    if request.method == "POST":  
        form = ProyekForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/home')  
            except:  
                return redirect('/home') 
    else:  
        form = ProyekForm()  
    return render(request,'index.html',{'form':form})

def ganti_proyek(request, id):  
    proyek = Proyek.objects.get(id=id)  
    form = ProyekForm(request.POST, instance = proyek)  
    if form.is_valid():  
        form.save()  
        return redirect("/home")  
    return render(request, 'index.html', {'proyek': proyek})  

def destroy_proyek(request, id):  
    proyek = Proyek.objects.get(id=id)  
    proyek.delete()  
    return redirect('/home')   

def translasi(request):
    return render(request,'translasi.html')

def hasil(request):
    return render(request,'hasil.html')

def database(request):
    return render(request,'database.html')

# crud

def addproyek(request):
    return render(request,'index.html')