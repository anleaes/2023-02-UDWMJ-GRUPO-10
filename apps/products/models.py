from django.db import models
from categories.models import Category

# Create your models here.

class Product(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    date_fabrication = models.DateField('Data Fabricacao', auto_now=False, auto_now_add=False) 
    is_active = models.BooleanField('Ativo', default=False)
    photo = models.ImageField('Foto', upload_to='photos')
    doc = models.FileField('Documentos', upload_to='docs')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering =['id']

    def __str__(self):
        return self.name


#########
# FORMS #
#########

# No caminho "apps/products/" crie um arquivo "forms.py" e coloque o conteudo 
# para declarar o modelo no forms e exclua da visualizacao o campo user para 
# que nao fique visivel. Essa etapa é o carregamento do modelo para o forms.

from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('created_on' , 'updated_on',)
