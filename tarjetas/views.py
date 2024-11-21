from django.shortcuts import render, get_object_or_404, redirect
from .models import Tarjeta
from .forms import TarjetaForm
from django.contrib.auth.decorators import login_required

@login_required
def listar_tarjetas(request):
    tarjetas = Tarjeta.objects.filter(cliente=request.user)
    return render(request, 'tarjetas/listar_tarjetas.html', {'tarjetas': tarjetas})


def eliminar_tarjeta(request, id):
    tarjeta = get_object_or_404(Tarjeta, id=id, cliente=request.user) 
    tarjeta.delete()  # Elimina la tarjeta
    return redirect('tarjetas:listar_tarjetas')

def crear_tarjeta(request):
    if request.method == 'POST':
        form = TarjetaForm(request.POST)
        if form.is_valid():
            tarjeta = form.save(commit=False)
            tarjeta.cliente = request.user  # Asociar la tarjeta al usuario autenticado
            tarjeta.save()
            return redirect('tarjetas:listar_tarjetas')  # Redirige a la lista de tarjetas del usuario
    else:
        form = TarjetaForm()
    
    return render(request, 'tarjetas/crear_tarjeta.html', {'form': form})


def detalle_tarjeta(request, id):
    tarjeta = get_object_or_404(Tarjeta, id=id)
    return render(request, 'tarjetas/detalle_tarjeta.html', {'tarjeta': tarjeta})
