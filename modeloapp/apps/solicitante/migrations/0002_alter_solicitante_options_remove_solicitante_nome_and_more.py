# Generated by Django 4.1 on 2023-12-07 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitante', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='solicitante',
            options={'ordering': ['id'], 'verbose_name': 'Solicitante', 'verbose_name_plural': 'Solicitantes'},
        ),
        migrations.RemoveField(
            model_name='solicitante',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='solicitante',
            name='sobrenome',
        ),
        migrations.DeleteModel(
            name='Solicitacao',
        ),
    ]
