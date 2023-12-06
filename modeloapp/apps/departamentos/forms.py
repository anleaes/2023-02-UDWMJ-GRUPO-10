from django import forms
from .models import Departamento

class DepartamentoForm(forms.ModelForm):

    class Meta:
        model = Departamento
        exclude = ('created_on' , 'updated_on',)