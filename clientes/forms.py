# clientes/forms.py
from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre' ,'apellido', 'dni','fecha_nacimiento', 'telefono', 'email']
