from django.urls import path
from . import views

app_name = "estoque"

urlpatterns = [
    path("", views.index, name = "index"),
    path("cadastroCategoria/", views.cadastroCategoria, name = "cadastroCategoria"),
    path("buscaCategoria/", views.buscaCategoria, name = "buscaCategoria"),
    path("cadastroProduto/", views.cadastroProduto, name = "cadastroProduto"),
    path("buscaProduto/", views.buscaProduto, name = "buscaProduto"),

]