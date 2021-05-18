from django import forms  
from cdg.models import Proyek
class ProyekForm(forms.ModelForm):  
    class Meta:  
        model = Proyek 
        fields = "__all__"  