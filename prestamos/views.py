from django.shortcuts import render, redirect, get_object_or_404
from .forms import PrestamoForm
from clientes.models import Cliente  # Importamos Cliente desde la app 'clientes'
from django.contrib.auth.decorators import login_required  # Decorador para asegurar que el usuario esté autenticado
from prestamos.models import Prestamo
from django.shortcuts import get_object_or_404

from cuentas.models import Cuenta

@login_required
def listar_prestamos(request):
    cliente = get_object_or_404(Cliente, user=request.user)  
    prestamos = cliente.prestamo_set.all()  # Supongo que un cliente puede tener varios préstamos asociados, ajusta según tu modelo

    return render(request, 'prestamos/listar_prestamos.html', {'prestamos': prestamos})


def detalle_prestamo(request, prestamo_id):
    # Usamos get_object_or_404 para obtener el préstamo o devolver un error 404 si no se encuentra
    prestamo = get_object_or_404(Prestamo, id=prestamo_id)
    return render(request, 'prestamos/detalle_prestamo.html', {'prestamo': prestamo})
def crear_prestamo(request):
    if not request.user.is_authenticated:
        return redirect('login:login')  # Redirigir al login si no está autenticado

    cliente = Cliente.objects.get(user=request.user)  # Obtenemos el cliente logueado
    cuenta = Cuenta.objects.get(cliente=cliente)  # Obtenemos la cuenta asociada al cliente

    if request.method == 'POST':
        form = PrestamoForm(request.POST, cliente=cliente)  # Pasamos el cliente al formulario
        if form.is_valid():
            prestamo = form.save(commit=False)  # Inicializamos el prestamo primero
            prestamo.cliente = cliente  # Aseguramos que el cliente se asocia correctamente
            prestamo.cuenta = form.cleaned_data['cuenta']  # Asociamos la cuenta seleccionada
            prestamo.aprobado = False  # Inicializamos el estado de aprobado

            # Verificación de los límites por tipo de cuenta
            if (prestamo.cuenta.tipo == 'CLASSIC') and (prestamo.monto <= 100000):
                prestamo.aprobado = True
            elif (prestamo.cuenta.tipo == 'GOLD') and (prestamo.monto <= 300000):
                prestamo.aprobado = True
            elif (prestamo.cuenta.tipo == 'BLACK') and (prestamo.monto <= 500000):
                prestamo.aprobado = True

            if prestamo.aprobado:
                cuenta.saldo += prestamo.monto  # Aumentamos el saldo de la cuenta
                cuenta.save()
                prestamo.save()
                return redirect('prestamos:detalle_prestamo', prestamo_id=prestamo.id)
            else:
                return render(request, 'prestamos/crear_prestamo.html', {'error': 'Cuenta no autorizada para solicitar ese monto.'})

    else:
        form = PrestamoForm(cliente=cliente)  # Al pasar el cliente, el formulario puede usarlo

    return render(request, 'prestamos/crear_prestamo.html', {'form': form})
