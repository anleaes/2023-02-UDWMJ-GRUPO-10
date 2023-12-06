from django.db import models
from usuarios.models import Usuario

class Atendimento(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    data = models.DateField(verbose_name='Data')
    hora = models.TimeField(verbose_name='Hora')

    atendimento_user = models.ManyToManyField(Usuario, through='AtendimentoUser', blank=True)
    
    class Meta:
        verbose_name = 'Atendimento'
        verbose_name_plural = 'Atendimentos'
        ordering =['id']

    def __str__(self):
        return self.data


class AtendimentoUser(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    atendimento = models.ForeignKey(Atendimento, on_delete=models.CASCADE)
    username = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuário'
        ordering =['id']

    def __str__(self):
        return self.usuario.username