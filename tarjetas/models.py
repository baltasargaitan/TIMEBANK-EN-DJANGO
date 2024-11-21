from django.db import models
from django.contrib.auth.models import User  

class Tarjeta(models.Model):
    TIPO_CHOICES = [
        ('DEBITO', 'Débito'),
        ('CREDITO', 'Crédito'),
    ]
    
    numero = models.CharField(max_length=16, unique=True)  # Número de la tarjeta
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='DEBITO')
    fecha_vencimiento = models.DateField()
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tarjetas')  # Relación con el cliente

    def __str__(self):
        return f"Tarjeta {self.numero} ({self.tipo})"
