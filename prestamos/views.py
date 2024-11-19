from django.shortcuts import render
from django.shortcuts import render
from .forms import SolicitudPrestamoForm

from django.shortcuts import render, get_object_or_404, redirect
from .models import Prestamo
from .forms import SolicitudPrestamoForm

def listar_prestamos(request):
    prestamos = Prestamo.objects.all()
    return render(request, 'prestamos/listar_prestamos.html', {'prestamos': prestamos})

def solicitar_prestamo(request):
    if request.method == 'POST':
        form = SolicitudPrestamoForm(request.POST)
        if form.is_valid():
            # Procesar formulario
            pass
    else:
        form = SolicitudPrestamoForm()
    return render(request, 'prestamos/solicitar_prestamo.html', {'form': form})

def detalle_prestamo(request, id):
    prestamo = get_object_or_404(Prestamo, id=id)
    return render(request, 'prestamos/detalle_prestamo.html', {'prestamo': prestamo})
