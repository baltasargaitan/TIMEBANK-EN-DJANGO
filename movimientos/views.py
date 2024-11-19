from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Movimiento

def listar_movimientos(request):
    movimientos = Movimiento.objects.all()
    return render(request, 'movimientos/listar_movimientos.html', {'movimientos': movimientos})

def crear_movimiento(request):
    if request.method == 'POST':
        # Procesar creación de movimiento
        pass
    return render(request, 'movimientos/crear_movimiento.html')

def detalle_movimiento(request, id):
    movimiento = get_object_or_404(Movimiento, id=id)
    return render(request, 'movimientos/detalle_movimiento.html', {'movimiento': movimiento})
