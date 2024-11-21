from django.shortcuts import render, redirect, get_object_or_404
from .forms import PrestamoForm
from clientes.models import Cliente  # Importamos Cliente desde la app 'clientes'
from django.contrib.auth.decorators import login_required  # Decorador para asegurar que el usuario esté autenticado
from prestamos.models import Prestamo
from django.shortcuts import get_object_or_404




def detalle_prestamo(request, prestamo_id):
    # Usamos get_object_or_404 para obtener el préstamo o devolver un error 404 si no se encuentra
    prestamo = get_object_or_404(Prestamo, id=prestamo_id)
    
    # Si el préstamo no pertenece al cliente logueado, se puede redirigir o mostrar un error
    if prestamo.cliente.user != request.user:
        return redirect('prestamos:listar_prestamos')  # Redirigir al listado de préstamos si no es el cliente correcto
    
    return render(request, 'prestamos/detalle_prestamo.html', {'prestamo': prestamo})
def crear_prestamo(request):
    if not request.user.is_authenticated:
        return redirect('login:login')  # Redirigir al login si no está autenticado

    cliente = Cliente.objects.get(user=request.user)  # Obtenemos el cliente logueado
    
    if request.method == 'POST':
        form = PrestamoForm(request.POST, cliente=cliente)
        if form.is_valid():
            prestamo = form.save(commit=False)
            prestamo.cliente = cliente
            # Verificamos si el saldo es suficiente
            if prestamo.monto <= cliente.saldo:
                prestamo.aprobado = True  # Aprobamos el préstamo si hay suficiente saldo
                cliente.saldo -= prestamo.monto  # Reducimos el saldo de la cuenta
                cliente.save()
                prestamo.save()
                return redirect('prestamos:detalle_prestamo', pk=prestamo.pk)  # Redirigimos al detalle del préstamo
            else:
                form.add_error('monto', 'Saldo insuficiente para este préstamo.')
    else:
        form = PrestamoForm(cliente=cliente)
    
    return render(request, 'prestamos/crear_prestamo.html', {'form': form})


@login_required
def listar_prestamos(request):
    cliente = get_object_or_404(Cliente, user=request.user)  
    prestamos = cliente.prestamo_set.all()  # Supongo que un cliente puede tener varios préstamos asociados, ajusta según tu modelo

    return render(request, 'prestamos/listar_prestamos.html', {'prestamos': prestamos})
