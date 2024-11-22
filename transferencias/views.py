from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from .models import Transferencia
from cuentas.models import Cuenta
from django.contrib.auth.decorators import login_required

@login_required
def crear_transferencia(request):
    if request.method == 'POST':
        origen_id = request.POST.get('origen')
        destino_id = request.POST.get('destino')
        monto = request.POST.get('monto')

        # Convertir monto a Decimal para evitar el error de tipo
        monto_decimal = Decimal(monto)

        # Obtener las cuentas
        origen = get_object_or_404(Cuenta, id=origen_id, cliente__user=request.user)  # La cuenta de origen debe pertenecer al usuario logueado
        destino = get_object_or_404(Cuenta, id=destino_id)  # La cuenta de destino puede ser de cualquier cliente

        # Verificamos que la cuenta de destino no sea la misma que la cuenta de origen
        if origen == destino:
            return render(request, 'transferencias/crear_transferencia.html', {
                'error': 'No puedes transferir a tu propia cuenta', 
                'cuentas': Cuenta.objects.filter(cliente__user=request.user), 
                'cuentas_destino': Cuenta.objects.exclude(cliente__user=request.user), 
                'origen_id': origen_id, 
                'destino_id': destino_id, 
                'monto': monto
            })

        # Verificar si el saldo es suficiente
        if origen.saldo >= monto_decimal:
            origen.saldo -= monto_decimal
            destino.saldo += monto_decimal

            # Guardar las actualizaciones de las cuentas
            origen.save()
            destino.save()

            # Crear la transferencia
            transferencia = Transferencia.objects.create(origen=origen, destino=destino, monto=monto_decimal, estado='completada')

            return redirect('transferencias:detalle_transferencia', transferencia_id=transferencia.id)
        else:
            # Agregar un error si no hay suficiente saldo
            return render(request, 'transferencias/crear_transferencia.html', {
                'error': 'Saldo insuficiente',
                'cuentas': Cuenta.objects.filter(cliente__user=request.user),
                'cuentas_destino': Cuenta.objects.exclude(cliente__user=request.user),
                'origen_id': origen_id,
                'destino_id': destino_id,
                'monto': monto
            })

    # Si es un GET, mostramos el formulario de transferencia
    cuentas = Cuenta.objects.filter(cliente__user=request.user)  # Mostrar las cuentas del usuario logueado
    cuentas_destino = Cuenta.objects.exclude(cliente__user=request.user)  # Cuentas de otros usuarios

    return render(request, 'transferencias/crear_transferencia.html', {
        'cuentas': cuentas,
        'cuentas_destino': cuentas_destino
    })
def detalle_transferencia(request, transferencia_id):
    transferencia = get_object_or_404(Transferencia, id=transferencia_id)
    return render(request, 'transferencias/detalle_transferencia.html', {'transferencia': transferencia})
