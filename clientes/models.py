from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  # Relación uno a uno con el modelo User
    nombre = models.CharField(max_length=100, blank=True)  # Permitimos que estén vacíos inicialmente
    apellido = models.CharField(max_length=100, blank=True)
    dni = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)  # Usamos el email del usuario
    telefono = models.CharField(max_length=15, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.user.username})"
