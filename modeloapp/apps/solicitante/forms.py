from django import forms
from .models import Solicitante

class SolicitanteForm(forms.ModelForm):
    class Meta:
        model = Solicitante
        fields = ['nome', 'sobrenome', 'cpf']