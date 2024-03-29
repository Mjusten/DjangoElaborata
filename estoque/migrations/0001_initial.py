# Generated by Django 2.2.7 on 2019-11-21 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('cd_categoria', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nm_categoria', models.CharField(max_length=200, verbose_name='Categoria')),
                ('sg_categoria', models.CharField(max_length=6, verbose_name='Abreviação Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('cd_produto', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição')),
                ('descricao_abreviada', models.CharField(max_length=50, verbose_name='Descrição Abreviada')),
                ('codigo_barras', models.CharField(max_length=14, verbose_name='Código de Barras')),
                ('quantidade', models.IntegerField(verbose_name='Quantidade')),
                ('posicao', models.CharField(max_length=50, verbose_name='Posição')),
                ('fk_categoria', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='estoque.Categoria', verbose_name='Categoria')),
            ],
        ),
    ]
