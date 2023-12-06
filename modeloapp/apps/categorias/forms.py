from django import forms
from .models import Categorias

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Categorias
        exclude = ('nome' , 'descricao', 'departamento')