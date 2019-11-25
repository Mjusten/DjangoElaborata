from django.urls import path
from . import views

app_name="cliente"

urlpatterns = [
    path("", views.index , name="index" ),
    path("cadastroGenero/", views.cadastroGenero, name="cadastroGenero"),
    path("buscaGenero/", views.buscaGenero, name="buscaGenero"),
    path("cadastroCliente/", views.cadastroCliente, name="cadastroCliente"),
    path("buscaCliente/", views.buscaCliente, name="buscaCliente"),
    #path("buscaCliente/<int:cliente>", views.buscaCliente, name="buscaClienteUm"),
]