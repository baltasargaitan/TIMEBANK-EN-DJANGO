from django import forms
from .models import Tarjeta

class TarjetaForm(forms.ModelForm):
    # Definir el campo fecha_vencimiento con un widget de tipo 'date'
    fecha_vencimiento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        error_messages={'invalid': 'Introduzca una fecha válida.'}
    )

    class Meta:
        model = Tarjeta
        fields = ['numero', 'tipo', 'fecha_vencimiento']  # Asegúrate de que 'fecha_vencimiento' esté aquí

