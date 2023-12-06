from django.db import models

# Create your models here.

class Endereco(models.Model):
    logradouro = models.CharField(max_length=100)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=9)
    complemento = models.CharField(max_length=100, blank=True, null=True)