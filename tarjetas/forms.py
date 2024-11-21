from django import forms
from .models import Tarjeta

class TarjetaForm(forms.ModelForm):
    class Meta:
        model = Tarjeta
        fields = ['numero', 'tipo', 'fecha_vencimiento']
