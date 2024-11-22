# Generated by Django 5.1.3 on 2024-11-21 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0003_remove_cuenta_numero_cuenta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='saldo',
            field=models.DecimalField(decimal_places=2, default=100000, max_digits=12),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='tipo',
            field=models.CharField(choices=[('BLACK', 'Black'), ('GOLD', 'Gold'), ('SILVER', 'Silver'), ('CLASSIC', 'Classic')], default='GOLD', max_length=10),
        ),
    ]
