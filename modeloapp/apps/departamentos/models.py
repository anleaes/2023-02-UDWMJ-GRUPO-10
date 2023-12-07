from django.db import models

# Create your models here.

class Departamento(models.Model):
    nome = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descricao', max_length=80, default='Nulo') 
    
    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering =['id']

    def __str__(self):
        return self.nome