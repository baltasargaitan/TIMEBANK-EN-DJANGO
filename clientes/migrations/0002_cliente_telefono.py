# Generated by Django 5.1.3 on 2024-11-19 03:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(default='Desconocido', max_length=20, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{9,15}$', 'Número de teléfono no válido')]),
            preserve_default=False,
        ),
    ]