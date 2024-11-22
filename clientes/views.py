from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from django.contrib.auth.decorators import login_required
@login_required

def ver_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'clientes/ver_cliente.html', {'cliente': cliente})
from .models import Cliente
from .forms import ClienteForm  # Asegúrate de crear este formulario


def completar_perfil(request):
    cliente = Cliente.objects.get(user=request.user)
    
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('homebanking:homebanking')  # Redirigir a una página principal o dashboard
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'clientes/completar_perfil.html', {'form': form})