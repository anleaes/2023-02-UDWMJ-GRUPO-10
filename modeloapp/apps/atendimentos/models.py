from django.db import models
from solicitacoes.models import Solicitacao

# Create your models here.

class Atendimento(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    id_solicitacao = models.ForeignKey(Solicitacao, on_delete=models.CASCADE)
    data = models.DateField(verbose_name='Data')
    hora = models.TimeField(verbose_name='Hora')
    DEPARTAMENTO_CHOICES = (
        ('Departamento de Infraestrutura', 'Departamento de Infraestrutura'),
        ('Departamento de Iluminação Pública', 'Departamento de Iluminação Pública'),
        ('Departamento de Mobilidade Urbana', 'Departamento de Mobilidade Urbana'),
        ('Departamento de Infraestrutura', 'Departamento de Infraestrutura'),#
        ('Departamento de Serviços Ambientais e Limpeza Urbana', 'Departamento de Serviços Ambientais e Limpeza Urbana'),
        ('Departamento de Água e Saneamento', 'Departamento de Água e Saneamento'),
        ('Departamento de Energia', 'Departamento de Energia'),
        ('Selecionar', 'Selecionar'),
    )
    departamento = models.CharField('Departamento', max_length=100, choices=DEPARTAMENTO_CHOICES, null=True, blank=True, default='Selecionar')
    rua = models.CharField('Rua', max_length=200)
    numero = models.IntegerField('Número')
    bairro = models.CharField('Bairro', max_length=100)
    complemento = models.CharField('Complemento', max_length=100, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering =['-created_on']

    def __str__(self):
        return "%s" % (self.data)