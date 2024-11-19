from django.db import models
from clientes.models import Cliente
from cuentas.models import Cuenta

class Prestamo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    tipo_prestamo = models.CharField(
        max_length=20,
        choices=[('BLACK', 'Black'), ('GOLD', 'Gold'), ('CLASSIC', 'Classic')]
    )
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=20,
        choices=[('APROBADO', 'Aprobado'), ('RECHAZADO', 'Rechazado')],
        default='APROBADO'
    )

    def __str__(self):
        return f"Préstamo {self.tipo_prestamo} - {self.monto} ({self.cliente.nombre})"
