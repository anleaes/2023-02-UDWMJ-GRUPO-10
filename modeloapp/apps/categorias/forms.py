from django import forms
from .models import Categorias

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categorias
        exclude = ('nome' , 'descricao', 'departamento')