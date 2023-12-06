
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuarios(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Solicitacao(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Solicitacao'
        verbose_name_plural = 'Solicitacoes'
        ordering =['id']
    
#class Atendimento(models.Model):
#    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
        
class Solicitante(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Solicitante'
        verbose_name_plural = 'Solicitantes'
        ordering =['id']
