from django.db import models

# Create your models here.

class Servico(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    descricao = models.TextField('Descrição', max_length=500)
    status = models.CharField(max_length=100)

    class Meta:
            verbose_name = 'Serviço'
            verbose_name_plural = 'Serviços'
            ordering =['id']

    def __str__(self):
          return self.descricao
