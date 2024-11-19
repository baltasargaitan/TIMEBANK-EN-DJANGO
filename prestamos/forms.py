from django import forms

class SolicitudPrestamoForm(forms.Form):
    tipo_prestamo = forms.ChoiceField(choices=[('BLACK', 'Black'), ('GOLD', 'Gold'), ('CLASSIC', 'Classic')])
    monto = forms.DecimalField(max_digits=10, decimal_places=2)
    fecha_inicio = forms.DateField(widget=forms.SelectDateWidget)
