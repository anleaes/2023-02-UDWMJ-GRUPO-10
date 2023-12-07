from django.db import models

# Create your models here.

class Materiais(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    quantidade = models.IntegerField()
    valorUnitario = models.FloatField()

    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materiais'
        ordering =['id']

    def __str__(self):
        return self.nome