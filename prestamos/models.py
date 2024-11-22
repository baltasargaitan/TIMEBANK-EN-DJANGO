from django.db import models
from clientes.models import Cliente
from datetime import datetime
from cuentas.models import Cuenta

class Prestamo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_inicio = models.DateField(default=datetime.today)
    aprobado = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Préstamo de {self.monto} para {self.cliente.user.username}"
