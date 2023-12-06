from django import forms
from .models import atendimento

class AtendimentoForm(forms.ModelForm):

    class Meta:
        model = atendimento
        exclude = ('created_on' , 'updated_on',)