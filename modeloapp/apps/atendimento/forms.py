from django import forms
from .models import Atendimento

class AtendimentoForm(forms.ModelForm):
    data = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    class Meta:
        model = Atendimento
        exclude = ('created_on' , 'updated_on',)