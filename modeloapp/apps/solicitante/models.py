from django.db import models

# Create your models here.

class Solicitante(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    
class Solicitacao(models.Model):
    solicitante = models.ForeignKey(Solicitante, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Solicitante'
        verbose_name_plural = 'Solicitantes'
        ordering =['id']

class Usuarios(models.Model):
    solicitante = models.ForeignKey(Solicitante, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Solicitante'
        verbose_name_plural = 'Solicitantes'
        ordering =['id']

