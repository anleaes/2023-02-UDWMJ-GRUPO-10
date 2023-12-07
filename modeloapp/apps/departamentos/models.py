from django.db import models

# Create your models here.

class Departamento(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    nome = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descricao', max_length=80, default='Nulo') 
    
    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering =['id']

    def __str__(self):
        return self.nome