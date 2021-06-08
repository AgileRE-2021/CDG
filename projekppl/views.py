from cdg.models import Proyek, Proses, BPMN, DataObject, Database, Entitas, Atribut, Relasi
from projekppl.forms import ProyekForm, ProsesForm, BPMNForm, DataObjectForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from xml.dom import minidom

import re

def splash(request):
    return render(request, 'splash.html')

#inisiasi proyek
def home(request):   
    proyek = Proyek.objects.all()
    return render(request,'index.html',{'posts':proyek})

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

def upload_database(request, id):
    proyek = Proyek.objects.get(id=id)
    #proyek2 = Proyek.objects.filter(proyek_id=proses.proyek_id)
    if request.method == 'POST':
        if proyek.database_id is None:
            file_database = request.FILES['fileDatabase']
            nama_database = file_database.name
            file = FileSystemStorage()
            file.save(file_database.name, file_database)

            basisdata = Database(nama_database=nama_database, proyek_id=id)
            basisdata.save()
            proyek.database_id = basisdata.id
            proyek.save()

            file_database = open(settings.BASE_DIR + '/media/' + file_database.name)
            info_database = minidom.parse(file_database)
            basisdata_parse = info_database.getElementsByTagName('pma:table')
            for elem in basisdata_parse:
                entitas = elem.attributes['name'].value #ambil nama tabel/entitas
                id_database = Database.objects.latest('id')
                entitas2 = Entitas(nama_entitas=entitas, database_id=id_database.id)
                entitas2.save()

                atribut = elem.firstChild.nodeValue #ambil text dari tag 'name'
                id_entitas = Entitas.objects.latest('id')

                atribut2 = re.findall(r"(?<=  `)[a-zA-Z0-9_]+(?=\W*`)", atribut) #filtering buat ambil atribut dari variable 'atribut'
                tipe_data = re.findall(r"(?<=` )[a-zA-Z0-9_]+(?=\W*\(| N)", atribut)  # filtering buat ambil tipe data dari variable 'atribut'
                iterasi=0
                for i in atribut2:
                    atribut3 = Atribut(nama_atribut=atribut2[iterasi], entitas_id=id_entitas.id, tipe_data=tipe_data[iterasi])
                    atribut3.save()
                    iterasi=iterasi+1

                relasi = re.findall(r"(?<=REFERENCES `)[a-zA-Z0-9_]+(?=\W*`)", atribut) #filter buat ambil relasi dari variable 'atribut'
                iterasi = 0
                for j in relasi:
                    relasi2 = Relasi(berelasi_dengan=relasi[iterasi], entitas_id=id_entitas.id)
                    relasi2.save()
                    iterasi = iterasi+1
        else:
            file_database = request.FILES['fileDatabase']
            nama_database = file_database.name
            file = FileSystemStorage()
            file.save(file_database.name, file_database)

            Database.objects.filter(proyek_id=id).delete()

            basisdata = Database(nama_database=nama_database, proyek_id=id)
            basisdata.save()
            proyek.database_id = basisdata.id
            proyek.save()

            file_database = open(settings.BASE_DIR + '/media/' + file_database.name)
            info_database = minidom.parse(file_database)
            basisdata_parse = info_database.getElementsByTagName('pma:table')
            for elem in basisdata_parse:
                entitas = elem.attributes['name'].value  # ambil nama tabel/entitas
                id_database = Database.objects.latest('id')
                entitas2 = Entitas(nama_entitas=entitas, database_id=id_database.id)
                entitas2.save()

                atribut = elem.firstChild.nodeValue  # ambil text dari tag 'name'
                id_entitas = Entitas.objects.latest('id')

                atribut2 = re.findall(r"(?<=  `)[a-zA-Z0-9_]+(?=\W*`)",
                                      atribut)  # filtering buat ambil atribut dari variable 'atribut'
                tipe_data = re.findall(r"(?<=` )[a-zA-Z0-9_]+(?=\W*\()",
                                       atribut)  # filtering buat ambil tipe data dari variable 'atribut'
                iterasi = 0
                for i in atribut2:
                    atribut3 = Atribut(nama_atribut=atribut2[iterasi], entitas_id=id_entitas.id, tipe_data=tipe_data[iterasi])
                    atribut3.save()
                    iterasi = iterasi + 1

                relasi = re.findall(r"(?<=REFERENCES `)[a-zA-Z0-9_]+(?=\W*`)",
                                    atribut)  # filter buat ambil relasi dari variable 'atribut'
                iterasi = 0
                for i in relasi:
                    relasi2 = Relasi(berelasi_dengan=relasi[iterasi], entitas_id=id_entitas.id)
                    relasi2.save()
                    iterasi = iterasi+1

        print(entitas)
        print(atribut2)
        print(relasi)

    return render(request,'database.html', {'proyek' : proyek})

def upload_bpmn(request, id):
    proses = Proses.objects.get(id=id)
    proses2 = Proses.objects.filter(proyek_id=proses.proyek_id)
    if request.method == 'POST':
        if proses.bpmn_id is None:
            file_bpmn = request.FILES['bpmn']
            nama_bpmn = file_bpmn.name
            file = FileSystemStorage()
            file.save(file_bpmn.name, file_bpmn)
            bpmn = BPMN(nama_bpmn=nama_bpmn, proses_id=id)
            bpmn.save()
            print("ini adalah :", bpmn.id)
            #BPMN.objects.create(proses=id, nama_bpmn=nama_bpmn)
            proses.bpmn_id = bpmn.id
            proses.save()
            file_bpmn = open(settings.BASE_DIR+'/media/'+file_bpmn.name)
            info_bpmn = minidom.parse(file_bpmn)
            data_object = info_bpmn.getElementsByTagName('DataObject')
            for elem in data_object:
                bpmn2 = BPMN.objects.latest('id')
                nama_elem = elem.attributes['Name'].value
                nama_lower = nama_elem.lower()
                if nama_lower[-1] == " ":
                    nama_lower = nama_lower[:-1]
                nama_hasil = nama_lower.replace(" ", "_")
                data = DataObject(bpmn_id=bpmn2.id, nama_data_objek=nama_hasil, state=elem.attributes['State'].value)
                #DataObject.objects.create(bpmn=id_bpmn, nama_data_objek=elem.attributes['Name'].value, state=elem.attributes['State'].value)
                data.save()
                #path = settings.MEDIA_ROOT
                #os.remove(os.path.join(path, file_bpmn.replace('/', '\\')))
        else: 
            file_bpmn = request.FILES['bpmn']
            nama_bpmn = file_bpmn.name
            file = FileSystemStorage()
            file.save(file_bpmn.name, file_bpmn)
            model_bpmn = BPMN.objects.get(id=proses.bpmn_id)
            model_bpmn.nama_bpmn = nama_bpmn
            model_bpmn.save()

            file_bpmn = open(settings.BASE_DIR+'/media/'+file_bpmn.name)
            info_bpmn = minidom.parse(file_bpmn)
            data_object = info_bpmn.getElementsByTagName('DataObject')
            for elem in data_object:
                data = DataObject.objects.get(bpmn_id=proses.bpmn_id)
                data.nama_data_objek = elem.attributes['Name'].value
                data.state = elem.attributes['State'].value
                data.save()
    return render(request,'translasi.html',{'posts':proses2 , 'idproyek' : proses.proyek_id}) 

def destroy_proyek(request, id):  
    proyek = Proyek.objects.get(id=id)  
    proyek.delete()  
    return redirect('/home')   

#translasi proyek
def translasi(request, id):
    proses = Proses.objects.filter(proyek_id=id)
    proyek = Proyek.objects.get(id=id)
    return render(request,'translasi.html',{'posts':proses , 'idproyek' : id , 'proyek':proyek})

def tambah_proses(request, id):
    proses = Proses.objects.filter(proyek_id=id)
    proyek = Proyek.objects.get(id=id)
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
            return render(request,'translasi.html',{'posts':proses , 'idproyek' : id , 'proyek':proyek})
        else:
            print("FORM GA VALID")
    context = {'form': form}
    return render (request, 'translasi.html', context=context)

def ganti_proses(request, id):  
    proses = Proses.objects.get(id=id)
    proyek = Proyek.objects.get(id=proses.proyek_id)
    proses2 = Proses.objects.filter(proyek_id=proses.proyek_id)
    form = ProsesForm(request.POST, instance = proses)  
    if form.is_valid():  
        form.save()  
        return render(request,'translasi.html',{'posts':proses2 , 'idproyek' : proses.proyek_id , 'proyek':proyek}) 
    return redirect('/home')  

def destroy_proses(request, id): 
     
    proses = Proses.objects.get(id=id)
    proses2 = Proses.objects.filter(proyek_id=proses.proyek_id)
    proyek = Proyek.objects.get(id=proses.proyek_id) 
    proses.delete()
    return render(request,'translasi.html',{'posts':proses2 , 'idproyek' : proses.proyek_id, 'proyek':proyek}) 

def hasil(request, id):
    proyek = Proyek.objects.get(id=id)
    return render(request,'hasil.html', {'proyek' : proyek})

#DATABASE

def database(request, id):
    proyek = Proyek.objects.get(id=id)
    return render(request,'database.html', {'proyek' : proyek})

#DOWNLOAD

def download(request, id):
    proyek = Proyek.objects.get(id=id)
    f = open(proyek.nama_proyek + ".txt","w+")

    proses = Proses.objects.filter(proyek_id=id)
    
    data_dict = {}
    #PENGAMBILAN NAMA CLASS dan STATE DARI DATAOBJECT
    array_class = []
    array_state = []
    for nilai in proses:
        data = DataObject.objects.filter(bpmn_id=nilai.bpmn_id)
        for nilai2 in data:
            array_class.append(nilai2.nama_data_objek)

    array_class = set(array_class)

    for nilai in proses:
        data = DataObject.objects.filter(bpmn_id=nilai.bpmn_id)
        i=0
        for nilai2 in data:
            if nilai2.nama_data_objek == array_class[i]:
                data_dict[array_class[i]].append(nilai2.state)
            i=i+1
    
    print(data_dict)
    #PENGAMBILAN NAMA CLASS DARI DATAOBJECT END
    
    #PENGAMBILAN ATRIBUT TIAP CLASS

    #PENGAMBILAN ATRIBUT TIAP CLASS END

    f.write(str(array_class))
    f.close()
    return render(request,'database.html', {'proyek' : proyek})