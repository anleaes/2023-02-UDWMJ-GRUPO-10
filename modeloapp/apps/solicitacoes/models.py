from django.db import models
from endereco.models import Endereco
from solicitante.models import Solicitante

# Create your models here.

class Solicitacao(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    solicitante_nome = models.ManyToManyField(Solicitante, through='NomeSolicitante', blank=True)
    CATEGORIA_CHOICES = (
        ('manutencao_de_infraestrutura_urbana', 'Manutenção de Infraestrutura Urbana'),
        ('gestao_de_residuos', 'Gestão de Resíduos'),
        ('servicos_de_utilidade_publica', 'Serviços de Utilidade Pública'),
    )
    categoria = models.CharField('Categoria', max_length=100, choices=CATEGORIA_CHOICES)
    descricao = models.TextField('Descrição', max_length=150) 
    solicitacao_endereco = models.ManyToManyField(Endereco, through='SolicitacaoEndereco', blank=True)
    
    class Meta:
        verbose_name = 'Solicitacao'
        verbose_name_plural = 'Solicitacoes'
        ordering =['id']

    def __str__(self):
        return self.descricao


class SolicitacaoEndereco(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    solicitacao = models.ForeignKey(Solicitacao, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Endereco'
        verbose_name_plural = 'Enderecos'
        ordering =['id']

    def __str__(self):
        return self.endereco.logradouro, self.endereco.numero
    
    class NomeSolicitante(models.Model):
        created_on = models.DateTimeField(auto_now_add=True)
        updated_on = models.DateTimeField(auto_now=True)
        solicitacao = models.ForeignKey(Solicitacao, on_delete=models.CASCADE)
        nome = models.ForeignKey(Solicitante, on_delete=models.CASCADE)

        class Meta:
            verbose_name = 'Solicitante'
            verbose_name_plural = 'Solicitantes'
            ordering =['id']

        def __str__(self):
            return self.solicitante.nome
    