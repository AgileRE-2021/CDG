from cdg.models import Proyek, Proses, BPMN, DataObject
from projekppl.forms import ProyekForm, ProsesForm, BPMNForm, DataObjectForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from xml.dom import minidom

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

def upload_bpmn(request, id):
    if request.method == 'POST':
        file_bpmn = request.FILES['bpmn']
        nama_bpmn = file_bpmn.name
        file = FileSystemStorage()
        file.save(file_bpmn.name, file_bpmn)
        bpmn = BPMN(nama_bpmn=nama_bpmn, proses_id=Proses.objects.get(proses_id=id))
        print("ini adalah :", bpmn)
        bpmn.save()
        #BPMN.objects.create(proses=id, nama_bpmn=nama_bpmn)

        file_bpmn = open(settings.BASE_DIR+'/media/'+file_bpmn.name)
        info_bpmn = minidom.parse(file_bpmn)
        data_object = info_bpmn.getElementsByTagName('DataObject')
        for elem in data_object:
            id_bpmn = BPMN.objects.latest('id')
            print(elem.attributes['Name'].value)
            print(elem.attributes['State'].value)
            data = DataObject(bpmn_id=id_bpmn, nama_data_objek=elem.attributes['Name'].value, state=elem.attributes['State'].value)
            #DataObject.objects.create(bpmn=id_bpmn, nama_data_objek=elem.attributes['Name'].value, state=elem.attributes['State'].value)
            data.save()
            #path = settings.MEDIA_ROOT
            #os.remove(os.path.join(path, file_bpmn.replace('/', '\\')))
    print('a')
    return render(request, 'translasi.html')

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