# Generated by Django 4.1 on 2023-12-06 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='descricao',
            field=models.CharField(choices=[('default', 'Selecione uma opção de serviço'), ('Reparos em estradas, calçadas, pontes', 'Reparos em estradas, calçadas, pontes'), ('Iluminação pública', 'Iluminação pública'), ('Sinalização viária', 'Sinalização viária'), ('Reciclagem', 'Reciclagem'), ('Coleta de lixo', 'Coleta de lixo'), ('Limpeza de áreas públicas', 'Limpeza de áreas públicas'), ('Fornecimento de água', 'Fornecimento de água'), ('Energia elétrica', 'Energia elétrica'), ('Manutenção de redes de esgoto', 'Manutenção de redes de esgoto')], default='default', max_length=50),
        ),
        migrations.AlterField(
            model_name='servico',
            name='status',
            field=models.CharField(choices=[('pendente', 'Pendente'), ('em_andamento', 'Em Andamento'), ('concluido', 'Concluído')], default='pendente', max_length=20),
        ),
    ]
