# Generated by Django 4.1 on 2023-12-08 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atendimentos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento',
            name='numero',
            field=models.IntegerField(verbose_name='Número'),
        ),
    ]
