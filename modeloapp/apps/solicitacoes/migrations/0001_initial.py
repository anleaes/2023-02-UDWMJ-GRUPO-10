# Generated by Django 4.1 on 2023-12-06 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('endereco', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('categoria', models.CharField(choices=[('manutencao_de_infraestrutura_urbana', 'Manutenção de Infraestrutura Urbana'), ('gestao_de_residuos', 'Gestão de Resíduos'), ('servicos_de_utilidade_publica', 'Serviços de Utilidade Pública')], max_length=100, verbose_name='Categoria')),
                ('descricao', models.TextField(max_length=150, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Solicitacao',
                'verbose_name_plural': 'Solicitacoes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SolicitacaoEndereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endereco.endereco')),
                ('solicitacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitacoes.solicitacao')),
            ],
            options={
                'verbose_name': 'Endereco',
                'verbose_name_plural': 'Enderecos',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='solicitacao',
            name='solicitacao_endereco',
            field=models.ManyToManyField(blank=True, through='solicitacoes.SolicitacaoEndereco', to='endereco.endereco'),
        ),
    ]
