from django.db import models

# Create your models here.

class Solicitante(models.Model):
    cpf = models.CharField(max_length=11, unique=True)
    
    class Meta:
        verbose_name = 'Solicitante'
        verbose_name_plural = 'Solicitantes'
        ordering =['id']

    def __str__(self):
        return self.cpf


