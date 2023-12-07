from django.db import models
from solicitante.models import Solicitante
from django import forms

class Usuarios(models.Model):
    usuarios = models.CharField('Usuario', max_length=50)
    email = models.EmailField('E-mail',null=False, blank=False)
    senha = models.CharField('Senha', max_length=50)
    usuarios_solicitante = models.ManyToManyField(Solicitante, through='UsuariosSolicitante', blank=True)
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Cadastro de Usuarios'
        ordering =['id']

    def __str__(self):
        return self.email
    
class UsuariosSolicitante(models.Model):
    nome = models.CharField('Nome', max_length=50) 
    sobrenome = models.CharField('Sobrenome', max_length=50)
    cpf = models.CharField('CPF', max_length=50)
    usuarios = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    solicitante = models.ForeignKey(Solicitante, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'UsuariosSolicitante'
        verbose_name_plural = 'UsuariosSolicitantes'
        ordering =['id']

    def __str__(self):
        return self.solicitante.nome
    
class LogoutForm(forms.Form):
    pass
