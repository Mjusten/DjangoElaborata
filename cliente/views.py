from django.shortcuts import render
from django.http import HttpResponse
from cliente.models import Genero, Cliente

#Formulários

from .forms import GeneroForm, ClienteForm

#Views

def index(request):

    context = {} #{"nome":"Batman"}

    return render(request, "cliente/index.html", context)

def cadastroGenero(request):

    if request.method == "GET":
        form = GeneroForm()
        context = { 
            "form" : form,
        }
        return render(request, "cliente/cadastroGenero.html", context)
    
    elif request.method == "POST":
    
        form = GeneroForm( request.POST )
        form.save()

        context = { 
            "sucesso" : "Gênero cadastrado com sucesso",
        }

        return render(request, "cliente/cadastroGenero.html", context)
    
    else: 
        return HttpResponse("<h2>Tá errado issaí</h2>")


def buscaGenero(request, cliente=0):

    busca = Genero.objects.all()

    context= {
        "generos":busca,
    }

    return render(request, "cliente/buscaGenero.html", context)


def cadastroCliente(request):

    if request.method == "GET":
        form = ClienteForm()
        context = { 
            "form" : form,
        }
        return render(request, "cliente/cadastroCliente.html", context)
    
    elif request.method == "POST":
    
        form = ClienteForm( request.POST )
        form.save()

        context = { 
            "sucesso" : "Cliente cadastrado com sucesso",
        }

        return render(request, "cliente/cadastroCliente.html", context)
    
    else: 
        return HttpResponse("<h2>Tá errado issaí</h2>")


def buscaCliente(request, cliente=0):

    busca = Cliente.objects.all()

    context= {
        "clientes":busca,
    }

    return render(request, "cliente/buscaCliente.html", context)
    
    
