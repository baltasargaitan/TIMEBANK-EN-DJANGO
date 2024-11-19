from django.db import models
from clientes.models import Cliente

class Tarjeta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    numero = models.CharField(max_length=16, unique=True)
    tipo_tarjeta = models.CharField(
        max_length=20,
        choices=[('CREDITO', 'Crédito'), ('DEBITO', 'Débito')],
        default='DEBITO'
    )
    fecha_vencimiento = models.DateField()

    def __str__(self):
        return f"Tarjeta {self.tipo_tarjeta} - {self.numero} ({self.cliente.nombre})"
