from cdg.models import Proyek, Proses
from projekppl.forms import ProyekForm, ProsesForm
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

def translasi(request, id):
    proses = Proses.objects.filter(proyek_id=id)
    return render(request,'translasi.html',{'posts':proses , 'idproyek' : id})

def tambah_proses(request, id):
    proses = Proses.objects.filter(proyek_id=id)
    form = ProsesForm()
    if request.method == 'POST':
        proyekID = Proyek.objects.get(id=id)
        form = ProsesForm(request.POST)
        print(form)
        if form.is_valid():
            print(form)
            formulir = form.save(commit=False)
            formulir.proyek = proyekID
            formulir.save()
            return render(request,'translasi.html',{'posts':proses , 'idproyek' : id})
        else:
            print("FORM GA VALID")
    context = {'form': form}
    return render (request, 'translasi.html', context=context)

def ganti_proses(request, id):  
    proses = Proses.objects.get(id=id)
    proses2 = Proses.objects.filter(proyek_id=proses.proyek_id)
    form = ProsesForm(request.POST, instance = proses)  
    if form.is_valid():  
        form.save()  
        return render(request,'translasi.html',{'posts':proses2 , 'idproyek' : proses.proyek_id}) 
    return redirect('/home')  

def destroy_proses(request, id):  
    proses = Proses.objects.get(id=id)
    proses2 = Proses.objects.filter(proyek_id=proses.proyek_id)
    proses.delete()  
    return render(request,'translasi.html',{'posts':proses2 , 'idproyek' : proses.proyek_id}) 

def hasil(request):
    return render(request,'hasil.html')

def database(request):
    return render(request,'database.html')

# crud

def addproyek(request):
    return render(request,'index.html')