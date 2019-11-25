from django import forms
from .models import Genero, Cliente

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = "__all__"

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"