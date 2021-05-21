from django import forms  
from cdg.models import Proyek
from cdg.models import Proses
class ProyekForm(forms.ModelForm):  
    class Meta:  
        model = Proyek 
        fields = "__all__"  

class ProsesForm(forms.ModelForm):  
    class Meta:  
        model = Proses 
        fields = ['nama_proses']  