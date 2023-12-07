from django.db import models

# Create your models here.

class Avaliacao(models.Model):
    nota = models.IntegerField()

    class Meta:
        verbose_name = 'Avaliacao'
        verbose_name_plural = 'Avaliacoes'
        ordering =['id']

    def __str__(self):
        return f'{self.nota}'