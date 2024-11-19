from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cuenta

def listar_cuentas(request):
    cuentas = Cuenta.objects.all()
    return render(request, 'cuentas/listar_cuentas.html', {'cuentas': cuentas})

def crear_cuenta(request):
    if request.method == 'POST':
        # Procesar creación de cuenta (puedes agregar un formulario aquí)
        pass
    return render(request, 'cuentas/crear_cuenta.html')

def detalle_cuenta(request, id):
    cuenta = get_object_or_404(Cuenta, id=id)
    return render(request, 'cuentas/detalle_cuenta.html', {'cuenta': cuenta})