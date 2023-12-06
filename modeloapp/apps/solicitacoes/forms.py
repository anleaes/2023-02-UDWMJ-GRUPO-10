from django import forms
from .models import Solicitacao

class SolicitacaoForm(forms.ModelForm):
    class Meta:
        model = Solicitacao
        fields = ['categoria', 'descricao', 'solicitacao_endereco']
