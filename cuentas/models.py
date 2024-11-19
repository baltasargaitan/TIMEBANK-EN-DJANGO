from django.db import models
class Cuenta(models.Model):
    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_cuenta = models.CharField(
        max_length=20,
        choices=[('CAJA_AHORRO', 'Caja de Ahorro'), ('CUENTA_CORRIENTE', 'Cuenta Corriente')],
        default='CAJA_AHORRO'
    )

    def __str__(self):
        return f"Cuenta de {self.cliente.nombre} ({self.tipo_cuenta})"

# Create your models here.
