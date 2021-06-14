from cdg.models import Proyek, Proses, BPMN, DataObject, Database, Entitas, Atribut, Relasi
from projekppl.forms import ProyekForm, ProsesForm, BPMNForm, DataObjectForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from xml.dom import minidom
import mimetypes
from django.http.response import HttpResponse
import re
import copy
import string    
import random

import os

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

            ## RANDOM FILE NAME

            S = 10  # number of characters in the string.  
            # call random.choices() string module to find the string in Uppercase + numeric data.  
            ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
            file_database.name = str(ran) + "_" + file_database.name


            file.save(file_database.name, file_database)

            basisdata = Database(nama_database=nama_database, proyek_id=id)
            basisdata.save()
            proyek.database_id = basisdata.id
            proyek.save()

            file_database = open(settings.BASE_DIR + '/media/' + file_database.name)
            info_database = minidom.parse(file_database)
            basisdata_parse = info_database.getElementsByTagName('pma:table')
            for elem in basisdata_parse:
                nama_elem = elem.attributes['name'].value
                nama_lower = nama_elem.lower()
                
                id_database = Database.objects.latest('id')
                entitas2 = Entitas(nama_entitas=nama_lower, database_id=id_database.id)
                entitas2.save()

                atribut = elem.firstChild.nodeValue #ambil text dari tag 'name'
                id_entitas = Entitas.objects.latest('id')

                atribut2 = re.findall(r"(?<=  `)[a-zA-Z0-9_]+(?=\W*`)", atribut) #filtering buat ambil atribut dari variable 'atribut'
                tipe_data = re.findall(r"(?<=` )[a-zA-Z0-9_]+(?=\W*\(| N| D)", atribut)  # filtering buat ambil tipe data dari variable 'atribut'
                iterasi=0
                for i in atribut2:
                    atribut3 = Atribut(nama_atribut=atribut2[iterasi], entitas_id=id_entitas.id, tipe_data=tipe_data[iterasi])
                    atribut3.save()
                    iterasi=iterasi+1

                relasi = re.findall(r"(?<=REFERENCES `)[a-zA-Z0-9_]+(?=\W*`)", atribut) #filter buat ambil relasi dari variable 'atribut'
                iterasi = 0
                for j in relasi:
                    nama_berelasi = relasi[iterasi].lower()
                    relasi2 = Relasi(berelasi_dengan=nama_berelasi, entitas_id=id_entitas.id)
                    relasi2.save()
                    iterasi = iterasi+1
        else:
            file_database = request.FILES['fileDatabase']
            nama_database = file_database.name
            file = FileSystemStorage()

            ## RANDOM FILE NAME

            S = 10  # number of characters in the string.  
            # call random.choices() string module to find the string in Uppercase + numeric data.  
            ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
            file_database.name = str(ran) + "_" + file_database.name

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
                nama_elem = elem.attributes['name'].value
                nama_lower = nama_elem.lower()
                
                id_database = Database.objects.latest('id')
                entitas2 = Entitas(nama_entitas=nama_lower, database_id=id_database.id)
                entitas2.save()

                atribut = elem.firstChild.nodeValue  # ambil text dari tag 'name'
                id_entitas = Entitas.objects.latest('id')

                atribut2 = re.findall(r"(?<=  `)[a-zA-Z0-9_]+(?=\W*`)",
                                      atribut)  # filtering buat ambil atribut dari variable 'atribut'
                tipe_data = re.findall(r"(?<=` )[a-zA-Z0-9_]+(?=\W*\(| N| D)",
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
                    nama_berelasi = relasi[iterasi].lower()
                    relasi2 = Relasi(berelasi_dengan=nama_berelasi, entitas_id=id_entitas.id)
                    relasi2.save()
                    iterasi = iterasi+1

    return render(request,'database.html', {'proyek' : proyek})

def upload_bpmn(request, id):
    proses = Proses.objects.get(id=id)
    proses2 = Proses.objects.filter(proyek_id=proses.proyek_id)
    if request.method == 'POST':
        if proses.bpmn_id is None:
            file_bpmn = request.FILES['bpmn']
            nama_bpmn = file_bpmn.name
            file = FileSystemStorage()

            ## RANDOM FILE NAME

            S = 10  # number of characters in the string.  
            # call random.choices() string module to find the string in Uppercase + numeric data.  
            ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
            file_bpmn.name = str(ran) + "_" + file_bpmn.name


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
                if (elem.attributes['Name'].value is None):
                    BPMN.objects.filter(id=proses.bpmn_id).delete()
                    html = "<html><body> TERDAPAT ERROR PADA FILE BPMN ANDA (NAMA DATA OBJECT TIDAK DIDAPAT) </body></html>"
                    return HttpResponse(html)

                nama_elem = elem.attributes['Name'].value

                if (nama_elem.find("#") != -1):
                    BPMN.objects.filter(id=proses.bpmn_id).delete()
                    html = "<html><body> TERDAPAT ERROR PADA FILE BPMN ANDA (NAMA DATA OBJECT TIDAK NORMAL, MUNGKIN MENGANDUNG KARAKTER ILEGAL (enter, simbol simbol)) </body></html>"
                    return HttpResponse(html)

                if (nama_elem.find("&") != -1):
                    BPMN.objects.filter(id=proses.bpmn_id).delete()
                    html = "<html><body> TERDAPAT ERROR PADA FILE BPMN ANDA (NAMA DATA OBJECT TIDAK NORMAL, MUNGKIN MENGANDUNG KARAKTER ILEGAL (enter, simbol simbol))  </body></html>"
                    return HttpResponse(html)

                try:
                    elem.attributes['State'].value
                except Exception as err:
                    BPMN.objects.filter(id=proses.bpmn_id).delete()
                    html = "<html><body> TERDAPAT ERROR PADA FILE BPMN ANDA (NAMA STATE DATA OBJECT TIDAK NORMAL) </body></html>"
                    return HttpResponse(html)
                
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

            ## RANDOM FILE NAME

            S = 10  # number of characters in the string.  
            # call random.choices() string module to find the string in Uppercase + numeric data.  
            ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
            file_bpmn.name = str(ran) + "_" + file_bpmn.name


            file.save(file_bpmn.name, file_bpmn)

            BPMN.objects.filter(id=proses.bpmn_id).delete()

            bpmn = BPMN(nama_bpmn=nama_bpmn, proses_id=id)
            bpmn.save()
            proses.bpmn_id = bpmn.id
            proses.save()

            file_bpmn = open(settings.BASE_DIR+'/media/'+file_bpmn.name)
            info_bpmn = minidom.parse(file_bpmn)
            data_object = info_bpmn.getElementsByTagName('DataObject')
            for elem in data_object:
                bpmn2 = BPMN.objects.latest('id')
                if (elem.attributes['Name'].value is None):
                    BPMN.objects.filter(id=proses.bpmn_id).delete()
                    html = "<html><body> TERDAPAT ERROR PADA FILE BPMN ANDA (NAMA DATA OBJECT TIDAK DIDAPAT) </body></html>"
                    return HttpResponse(html)

                try:
                    elem.attributes['State'].value
                except NameError:
                    BPMN.objects.filter(id=proses.bpmn_id).delete()
                    html = "<html><body> TERDAPAT ERROR PADA FILE BPMN ANDA (STATE DATA OBJECT TIDAK DIDAPAT) </body></html>"
                    return HttpResponse(html)
                else:
                    print("Variable is defined.")
                
                try:
                    elem.attributes['State'].value
                except Exception as err:
                    BPMN.objects.filter(id=proses.bpmn_id).delete()
                    html = "<html><body> TERDAPAT ERROR PADA FILE BPMN ANDA (NAMA STATE DATA OBJECT TIDAK NORMAL) </body></html>"
                    return HttpResponse(html)

                nama_elem = elem.attributes['Name'].value

                if (nama_elem.find("#") != -1):
                    BPMN.objects.filter(id=proses.bpmn_id).delete()
                    html = "<html><body> TERDAPAT ERROR PADA FILE BPMN ANDA (NAMA DATA OBJECT TIDAK NORMAL) </body></html>"
                    return HttpResponse(html)

                if (nama_elem.find("&") != -1):
                    BPMN.objects.filter(id=proses.bpmn_id).delete()
                    html = "<html><body> TERDAPAT ERROR PADA FILE BPMN ANDA (NAMA DATA OBJECT TIDAK NORMAL) </body></html>"
                    return HttpResponse(html)    

                nama_lower = nama_elem.lower()
                if nama_lower[-1] == " ":
                    nama_lower = nama_lower[:-1]
                nama_hasil = nama_lower.replace(" ", "_")



                data = DataObject(bpmn_id=bpmn2.id, nama_data_objek=nama_hasil, state=elem.attributes['State'].value)
                #DataObject.objects.create(bpmn=id_bpmn, nama_data_objek=elem.attributes['Name'].value, state=elem.attributes['State'].value)
                data.save()
                #path = settings.MEDIA_ROOT
                #os.remove(os.path.join(path, file_bpmn.replace('/', '\\')))
                
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
    
    nama_file = proyek.nama_proyek.replace(" ", "") + ".txt"

    f = open(nama_file,"w+")

    f.write("@startuml") 
    f.write("\n")

    proses = Proses.objects.filter(proyek_id=id)
    
    #PENGAMBILAN NAMA CLASS
    array_class = []
    for nilai in proses:
        data = DataObject.objects.filter(bpmn_id=nilai.bpmn_id)
        for nilai2 in data:
            array_class.append(nilai2.nama_data_objek)

    #MEMBUAT LIST NAMA CLASS MENJADI UNIK
    array_class_unique = []
    for x in array_class: 
        if x not in array_class_unique:
            array_class_unique.append(x)



    for x in range(len(array_class_unique)):
        #PENULISAN CLASS
        f.write ("class " + array_class_unique[x] + " { ")
        f.write("\n")

        try:
             entitas = Entitas.objects.filter(database_id=proyek.database_id).get(nama_entitas=array_class_unique[x])
        except Entitas.DoesNotExist:
            html = "<html><body> BPMN DAN DATABASE ANDA TIDAK SESUAI </body></html>"
            return HttpResponse(html)

        #PENULISAN ATRIBUT
        entitas = Entitas.objects.filter(database_id=proyek.database_id).get(nama_entitas=array_class_unique[x])
        atribut = Atribut.objects.filter(entitas_id=entitas.id)
        array_atribut=[]

        for nilai3 in atribut:
            array_atribut.append(nilai3.nama_atribut + " : " + nilai3.tipe_data)
        
        for o in range(len(array_atribut)):
            f.write(array_atribut[o])
            f.write("\n")

        #PENGAMBILAN STATE
        array_state = []
        data = DataObject.objects.filter(nama_data_objek=array_class_unique[x])
        for nilai2 in data:
            array_state.append(nilai2.state)
        
        #MEMBUAT LIST NAMA STATE MENJADI UNIK
        array_state_unique = []
        for k in array_state: 
            if k not in array_state_unique:
                array_state_unique.append(k)

        #MENULIS STATE
        for j in range(len(array_state_unique)):
            f.write(array_state_unique[j] +"()")
            f.write("\n")
            
        f.write("}")
        f.write("\n")
    
    table = []
    for x in range(len(array_class_unique)):
        entitas = Entitas.objects.filter(database_id=proyek.database_id).get(nama_entitas=array_class_unique[x])
        relasi = Relasi.objects.filter(entitas_id=entitas.id)
        
        for nilai5 in relasi:
            if (nilai5.berelasi_dengan in array_class_unique):
                row = []
                for c in range(1):
                    row.append(entitas.nama_entitas)
                    row.append(nilai5.berelasi_dengan)
                table.append(row)

    new_list = copy.deepcopy(table)

    new_table = copy.deepcopy(table)

    for t in range(len(new_list)):
        new_list[t].reverse()

    k = len(table)-1
    for o in range(len(table)):
        for p in range(k):
            if table[o] == new_list[o+p+1]:
                if table[o] in new_table:
                    index = new_table.index(table[o])
                    del new_table[index]
        k=k-1


    for g in range(len(new_table)):
        f.write(new_table[g][0] + " -- " + new_table[g][1])
        f.write("\n")

    f.write("@enduml") 
    f.close()
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = nama_file
    # Define the full file path
    filepath = BASE_DIR + '/' +filename
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response



def downloadpng(request, id):
    proyek = Proyek.objects.get(id=id)
    
    nama_file = proyek.nama_proyek.replace(" ", "") + ".txt"

    f = open(nama_file,"w+")
    f.write("@startuml") 
    f.write("\n")

    proses = Proses.objects.filter(proyek_id=id)
    
    #PENGAMBILAN NAMA CLASS
    array_class = []
    for nilai in proses:
        data = DataObject.objects.filter(bpmn_id=nilai.bpmn_id)
        for nilai2 in data:
            array_class.append(nilai2.nama_data_objek)

    #MEMBUAT LIST NAMA CLASS MENJADI UNIK
    array_class_unique = []
    for x in array_class: 
        if x not in array_class_unique:
            array_class_unique.append(x)



    for x in range(len(array_class_unique)):
        #PENULISAN CLASS
        f.write ("class " + array_class_unique[x] + " { ")
        f.write("\n")
        
        try:
             entitas = Entitas.objects.filter(database_id=proyek.database_id).get(nama_entitas=array_class_unique[x])
        except Entitas.DoesNotExist:
            html = "<html><body> BPMN DAN DATABASE ANDA TIDAK SESUAI </body></html>"
            return HttpResponse(html)

        #PENULISAN ATRIBUT
        
        atribut = Atribut.objects.filter(entitas_id=entitas.id)
        array_atribut=[]

        for nilai3 in atribut:
            array_atribut.append(nilai3.nama_atribut + " : " + nilai3.tipe_data)
        
        for o in range(len(array_atribut)):
            f.write(array_atribut[o])
            f.write("\n")

        #PENGAMBILAN STATE
        array_state = []
        data = DataObject.objects.filter(nama_data_objek=array_class_unique[x])
        for nilai2 in data:
            array_state.append(nilai2.state)
        
        #MEMBUAT LIST NAMA STATE MENJADI UNIK
        array_state_unique = []
        for k in array_state: 
            if k not in array_state_unique:
                array_state_unique.append(k)

        #MENULIS STATE
        for j in range(len(array_state_unique)):
            f.write(array_state_unique[j] +"()")
            f.write("\n")
            
        f.write("}")
        f.write("\n")
    
    table = []
    for x in range(len(array_class_unique)):
        entitas = Entitas.objects.filter(database_id=proyek.database_id).get(nama_entitas=array_class_unique[x])
        relasi = Relasi.objects.filter(entitas_id=entitas.id)
        
        for nilai5 in relasi:
            if (nilai5.berelasi_dengan in array_class_unique):
                row = []
                for c in range(1):
                    row.append(entitas.nama_entitas)
                    row.append(nilai5.berelasi_dengan)
                table.append(row)

    new_list = copy.deepcopy(table)

    new_table = copy.deepcopy(table)

    for t in range(len(new_list)):
        new_list[t].reverse()

    k = len(table)-1
    for o in range(len(table)):
        for p in range(k):
            if table[o] == new_list[o+p+1]:
                if table[o] in new_table:
                    index = new_table.index(table[o])
                    del new_table[index]
        k=k-1


    for g in range(len(new_table)):
        f.write(new_table[g][0] + " -- " + new_table[g][1])
        f.write("\n")

    f.write("@enduml")  
    f.close()

    
    os.system("python -m plantuml " + nama_file)

    file_gambar = proyek.nama_proyek.replace(" ", "") + ".png"

    filename = file_gambar

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


    filepath = BASE_DIR + '/' +filename

    try:
        with open(filepath, "rb") as f:
            return HttpResponse(f.read(), content_type="image/jpeg")
    except IOError:
        html = "<html><body> Komputer anda butut tidak support </body></html>"
        return HttpResponse(html)

