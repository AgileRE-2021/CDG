from django.contrib import admin
from .models import Generate, Proses, Proyek, BPMN, Database, Atribut, DataObject, Entitas, Relasi

admin.site.register(Generate)
admin.site.register(Atribut)
admin.site.register(Database)
admin.site.register(DataObject)
admin.site.register(BPMN)
admin.site.register(Proyek)
admin.site.register(Proses)
admin.site.register(Relasi)
admin.site.register(Entitas)

# Register your models here.
