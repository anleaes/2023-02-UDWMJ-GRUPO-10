
from django.db import models
from django.contrib.auth.models import User
from solicitante.models import Solicitante
from solicitacoes.models import Solicitacao


# Create your models here.

class Usuarios(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    soliciante = models.ForeignKey(Solicitante, on_delete=models.CASCADE)
    solicitacao = models.ForeignKey(Solicitacao, on_delete=models.CASCADE)

#class Atendimento(models.Model):
#    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
        

