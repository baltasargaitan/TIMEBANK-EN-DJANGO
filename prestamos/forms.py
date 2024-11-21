from django import forms
from .models import Prestamo

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['fecha_inicio', 'monto']

    def __init__(self, *args, **kwargs):
        self.cliente = kwargs.pop('cliente', None)
        super().__init__(*args, **kwargs)

    def clean_monto(self):
        monto = self.cleaned_data['monto']
        # Límite según el tipo de cliente
        if self.cliente.tipo_cliente == 'BLACK' and monto > 500000:
            raise forms.ValidationError("El monto supera el límite para clientes BLACK.")
        elif self.cliente.tipo_cliente == 'GOLD' and monto > 300000:
            raise forms.ValidationError("El monto supera el límite para clientes GOLD.")
        elif self.cliente.tipo_cliente == 'CLASSIC' and monto > 100000:
            raise forms.ValidationError("El monto supera el límite para clientes CLASSIC.")
        return monto
