from django.db import models
from solicitante.models import Solicitante

# Create your models here.

class Solicitacao(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    cpf = models.ForeignKey(Solicitante, on_delete=models.CASCADE, default='1')
    CATEGORIA_CHOICES = (
        ('manutencao_de_infraestrutura_urbana', 'Manutenção de Infraestrutura Urbana'),
        ('gestao_de_residuos', 'Gestão de Resíduos'),
        ('servicos_de_utilidade_publica', 'Serviços de Utilidade Pública'),
    )
    categoria = models.CharField('Categoria', max_length=100, choices=CATEGORIA_CHOICES)
    descricao = models.TextField('Descrição', max_length=150) 
    
    class Meta:
        verbose_name = 'Solicitacao'
        verbose_name_plural = 'Solicitacoes'
        ordering =['id']

    def __str__(self):
        return "%s" % (self.descricao)
