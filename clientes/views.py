from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClienteForm
from .models import Cliente

# Vista para listar los clientes
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/listar_clientes.html', {'clientes': clientes})

# Vista para crear un cliente
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes:listar_clientes')  # Redirigir a la lista de clientes
    else:
        form = ClienteForm()

    return render(request, 'clientes/crear_cliente.html', {'form': form})



def detalle_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'clientes/detalle_cliente.html', {'cliente': cliente})
