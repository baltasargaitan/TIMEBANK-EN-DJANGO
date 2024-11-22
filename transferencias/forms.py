# forms.py
from django import forms
from cuentas.models import Cuenta

class TransferenciaForm(forms.Form):
    origen = forms.ModelChoiceField(queryset=Cuenta.objects.none(), empty_label="Selecciona una cuenta")
    destino = forms.ModelChoiceField(queryset=Cuenta.objects.all(), empty_label="Selecciona una cuenta destino")
    monto = forms.DecimalField(max_digits=10, decimal_places=2)

    def __init__(self, *args, **kwargs):
        cliente = kwargs.pop('cliente')  # Recibimos el cliente para limitar las cuentas
        super().__init__(*args, **kwargs)
        self.fields['origen'].queryset = Cuenta.objects.filter(cliente=cliente)  # Solo las cuentas del cliente
