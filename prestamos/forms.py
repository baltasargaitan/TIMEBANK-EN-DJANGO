# forms.py
from django import forms
from .models import Prestamo
from clientes.models import Cliente
from cuentas.models import Cuenta  # Asegúrate de importar el modelo Cuenta

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['monto', 'cuenta']  # Incluye el campo cuenta si es necesario

    def __init__(self, *args, **kwargs):
        cliente = kwargs.pop('cliente', None)  # Obtener el cliente desde el view
        super(PrestamoForm, self).__init__(*args, **kwargs)

        # Si el cliente está pasado, filtra las cuentas asociadas a este cliente
        if cliente:
            self.fields['cuenta'].queryset = Cuenta.objects.filter(cliente=cliente)

    def clean_monto(self):
        monto = self.cleaned_data.get('monto')
        cuenta = self.cleaned_data.get('cuenta')
        
        # Verifica si el saldo de la cuenta es suficiente
        if cuenta and monto > cuenta.saldo:
            raise forms.ValidationError('Saldo insuficiente para este préstamo.')

        return monto

