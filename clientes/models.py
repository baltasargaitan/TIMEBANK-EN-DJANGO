from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=10, unique=True)
    fecha_nacimiento = models.DateField()
    email = models.EmailField(unique=True)
    telefono = models.CharField(
    max_length=20,
    validators=[RegexValidator(r'^\+?1?\d{9,15}$', 'Número de teléfono no válido')]
)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    def get_absolute_url(self):
        return reverse('clientes:detalle_cliente', kwargs={'pk': self.pk})