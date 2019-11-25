from django.db import models

# Create your models here.

class Categoria(models.Model):
    nm_categoria = models.CharField(verbose_name="Categoria", max_length=200)
    sg_categoria = models.CharField(verbose_name="Abreviação Categoria", max_length= 6)


class Produto(models.Model):
    nome = models.CharField(verbose_name = "Nome", max_length=100)
    descricao = models.CharField(verbose_name = "Descrição", max_length=200)
    descricao_abreviada = models.CharField(verbose_name = "Descrição Abreviada", max_length=50)
    codigo_barras = models.CharField(verbose_name = "Código de Barras", max_length=14)
    quantidade = models.IntegerField(verbose_name="Quantidade")
    posicao = models.CharField(verbose_name = "Posição", max_length=50)
    fk_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name= "Categoria", default=0) 