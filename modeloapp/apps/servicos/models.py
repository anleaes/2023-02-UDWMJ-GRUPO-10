from django.db import models

# Create your models here.

class Servico(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    DESCRICAO_CHOICES = (
        ('default', 'Selecione uma opção de serviço'),
        ('Reparos em estradas, calçadas, pontes','Reparos em estradas, calçadas, pontes'), #miu = Manutenção de Infraestrutura Urbana
        ('Iluminação pública','Iluminação pública'),
        ('Sinalização viária','Sinalização viária'),
        ('Reciclagem','Reciclagem'), #gr = Gestão de Resíduos
        ('Coleta de lixo','Coleta de lixo'),
        ('Limpeza de áreas públicas','Limpeza de áreas públicas'),
        ('Fornecimento de água','Fornecimento de água'), #sup = Serviços de Utilidade Pública
        ('Energia elétrica','Energia elétrica'),
        ('Manutenção de redes de esgoto','Manutenção de redes de esgoto'),
    )
    descricao = models.CharField(max_length=50, choices=DESCRICAO_CHOICES, default='default')    
    STATUS_CHOICES = (
        ('pendente', 'Pendente'),
        ('em_andamento', 'Em Andamento'),
        ('concluido', 'Concluído'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')

    class Meta:
            verbose_name = 'Serviço'
            verbose_name_plural = 'Serviços'
            ordering =['id']

    def __str__(self):
          return self.descricao
