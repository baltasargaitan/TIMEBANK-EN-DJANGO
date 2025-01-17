# Generated by Django 5.1.3 on 2024-11-21 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuenta',
            name='numero_cuenta',
            field=models.CharField(default='0000000000', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='saldo',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='tipo_cuenta',
            field=models.CharField(choices=[('Ahorros Pesos', 'Caja de ahorro en pesos'), ('Ahorros Dolares', 'Caja de ahorro en dólares'), ('Corriente', 'Cuenta corriente')], max_length=20),
        ),
    ]
