from django.db import models
from django.contrib.auth.models import User  # Importamos el modelo User

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)  # Relación uno a uno con el modelo User
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()
    saldo = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
