from django import forms  
from cdg.models import Proyek
from cdg.models import Proses
from cdg.models import DataObject
from cdg.models import BPMN

class ProyekForm(forms.ModelForm):  
    class Meta:  
        model = Proyek 
        fields = ['nama_proyek']  

class ProsesForm(forms.ModelForm):  
    class Meta:  
        model = Proses 
        fields = ['nama_proses']

class BPMNForm(forms.ModelForm):
    class Meta:
        model = BPMN
        fields = "__all__"

class DataObjectForm(forms.ModelForm):
    class Meta:
        model = DataObject
        fields = "__all__"