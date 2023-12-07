from django import forms
from .models import Materiais

class MateriaisForm(forms.ModelForm):
    class Meta:
        model = Materiais
        fields = ['nome', 'descricao', 'quantidade', 'valorUnitario']