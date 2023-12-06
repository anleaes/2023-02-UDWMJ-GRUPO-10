from django import forms
from .models import Solicitacao

class SolicitacaoForm(forms.ModelForm):
    class Meta:
        model = Solicitacao
        exclude = ('created_on' , 'updated_on',)
        fields = ['categoria', 'descricao', 'solicitacao_endereco']
