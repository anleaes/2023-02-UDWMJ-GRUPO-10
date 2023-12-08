from django import forms
from .models import Atendimento, Solicitacao

class AtendimentoForm(forms.ModelForm):
    
    class Meta:
        model = Atendimento
        exclude = ('id_solicitacao', 'created_on' , 'updated_on')
        data = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
        hora = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))