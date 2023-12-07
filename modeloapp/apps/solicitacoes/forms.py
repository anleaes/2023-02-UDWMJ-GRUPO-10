from django import forms
from .models import Solicitacao

class SolicitacaoForm(forms.ModelForm):
    class Meta:
        model = Solicitacao
        exclude = ('cpf', 'created_on' , 'updated_on',)
