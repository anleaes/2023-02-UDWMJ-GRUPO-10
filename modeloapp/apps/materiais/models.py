from django.db import models

# Create your models here.

class Materiais(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    quantidade = models.IntegerField()
    valorUnitario = models.FloatField()

    def __str__(self):
        return self.nome

    def materiaisNecessarios(self):
        materiais = Materiais.objects.all()
        return materiais