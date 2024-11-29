from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cuenta
from django.contrib.auth.decorators import login_required
@login_required
def listar_cuentas(request):
    # Obtener la cuenta asociada al cliente logueado
    cuentas = Cuenta.objects.filter(cliente__user=request.user)


    return render(request, 'cuentas/listar_cuentas.html', {'cuentas': cuentas})
def crear_cuenta(request):
    if request.method == 'POST':

        pass
    return render(request, 'cuentas/crear_cuenta.html')
from django.shortcuts import render, get_object_or_404
from .models import Cuenta
from django.contrib.auth.decorators import login_required

@login_required
def detalle_cuenta(request):
    # Obtener la cuenta asociada al cliente logueado
    cuenta = get_object_or_404(Cuenta, cliente__user=request.user)

    # Pasar la cuenta a la plantilla
    return render(request, 'cuentas/detalle_cuenta.html', {'cuenta': cuenta})
