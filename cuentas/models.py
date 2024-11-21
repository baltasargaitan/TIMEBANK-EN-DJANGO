from django.db import models
from clientes.models import Cliente  # Importamos Cliente desde la app clientes

class Cuenta(models.Model):
    TIPO_CUENTA_CHOICES = [
        ('BLACK', 'Black'),
        ('GOLD', 'Gold'),
        ('SILVER', 'Silver'),
        ('CLASSIC', 'Classic'),
    ]
    
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)  # Relación uno a uno con Cliente
    saldo = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    cvu = models.CharField(max_length=22)  # El CVU de la cuenta
    tipo = models.CharField(max_length=10, choices=TIPO_CUENTA_CHOICES)
    
    def __str__(self):
        return f"Cuenta {self.cvu} - {self.tipo}"
