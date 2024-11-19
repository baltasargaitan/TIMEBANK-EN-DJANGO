from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Tarjeta

def listar_tarjetas(request):
    tarjetas = Tarjeta.objects.all()
    return render(request, 'tarjetas/listar_tarjetas.html', {'tarjetas': tarjetas})

def crear_tarjeta(request):
    if request.method == 'POST':
        # Procesar creación de tarjeta
        pass
    return render(request, 'tarjetas/crear_tarjeta.html')

def detalle_tarjeta(request, id):
    tarjeta = get_object_or_404(Tarjeta, id=id)
    return render(request, 'tarjetas/detalle_tarjeta.html', {'tarjeta': tarjeta})
