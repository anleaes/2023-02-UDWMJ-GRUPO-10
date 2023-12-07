# Generated by Django 4.1 on 2023-12-07 01:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solicitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitante.solicitante')),
            ],
            options={
                'verbose_name': 'Solicitante',
                'verbose_name_plural': 'Solicitantes',
                'ordering': ['id'],
            },
        ),
    ]
