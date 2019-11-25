from django.shortcuts import render
from django.http import HttpResponse
from estoque.models import Categoria, Produto

# Formularios

from .forms import CategoriaForm, ProdutoForm

# Views

def index(request):
    context = {}

    return render(request, "estoque/index.html" , context)

def cadastroCategoria(request):
    
    if request.method == "GET":
        form = CategoriaForm()
        context = {
            "form" : form,
        }
        return render(request, "estoque/cadastroCategoria.html", context)

    elif request.method == "POST":
        form = CategoriaForm( request.POST ) 
        form.save()

        context = {
            "sucesso" : "Categoria cadastrada com sucesso",
        }
        return render (request, "estoque/cadastroCategoria.html", context)

    else:
        return HttpResponse("<h2> Erro Inesperado </h2>")


def buscaCategoria(request, produto=0): 
    
    busca = Categoria.objects.all()

    context={
        "categorias":busca,
    }

    return render(request, "estoque/buscaCategoria.html", context)

def cadastroProduto(request):
    
    if request.method == "GET":
        form = ProdutoForm()
        context = {
            "form" : form,
        }
        return render(request, "estoque/cadastroProduto.html", context)

    elif request.method == "POST":
        form = ProdutoForm( request.POST ) 
        form.save()

        context = {
            "sucesso" : "Produto cadastrado com sucesso",
        }
        return render (request, "estoque/cadastroProduto.html", context)

    else:
        return HttpResponse("<h2> Erro Inesperado </h2>")


def buscaProduto(request, produto=0): 
    
    busca = Produto.objects.all()

    context={
        "produtos":busca,
    }

    return render(request, "estoque/buscaProduto.html", context)
