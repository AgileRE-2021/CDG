from django.db import models

class Proyek(models.Model):
    nama_proyek = models.CharField(max_length=50)
    database_id = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.nama_proyek

class Generate(models.Model):
    proyek = models.OneToOneField(Proyek, on_delete=models.CASCADE)
    tanggal_generate = models.DateTimeField(auto_now=True)
    url_jpg = models.CharField(max_length=100)
    url_png = models.CharField(max_length=100)
    url_svg = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)

class Proses(models.Model):
    proyek = models.ForeignKey(Proyek, on_delete=models.CASCADE)
    nama_proses = models.CharField(max_length=50)
    bpmn_id = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.nama_proses

class Database(models.Model):
    proyek = models.OneToOneField(Proyek, on_delete=models.CASCADE, null=True)
    nama_database = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

class BPMN(models.Model):
    proses= models.OneToOneField(Proses, on_delete=models.CASCADE, null=True)
    nama_bpmn = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

class DataObject(models.Model):
    bpmn= models.ForeignKey(BPMN, on_delete=models.CASCADE, null=True)
    nama_data_objek = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.nama_data_objek

class Entitas(models.Model):
    database = models.ForeignKey(Database, on_delete=models.CASCADE)
    nama_entitas = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_entitas

class Atribut(models.Model):
    entitas = models.ForeignKey(Entitas, on_delete=models.CASCADE)
    nama_atribut = models.CharField(max_length=100)
    tipe_data = models.CharField(max_length=50)

    def __str__(self):
        return self.nama_atribut

class Relasi(models.Model):
    entitas = models.ForeignKey(Entitas, on_delete=models.CASCADE)
    berelasi_dengan = models.CharField(max_length=50, null=True)
    tipe_relasi = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id)