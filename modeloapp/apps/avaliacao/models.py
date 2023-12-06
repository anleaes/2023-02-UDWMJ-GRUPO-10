from django.db import models

# Create your models here.

class Avaliacao(models.Model):
    nota = models.IntegerField()

    def __str__(self):
        return f'{self.nota}'
    
class AvaliacaoModel:
    def __init__(self, nota):
        self.nota = nota

    def avaliar(self):
        return f'Avaliação: {self.nota}'