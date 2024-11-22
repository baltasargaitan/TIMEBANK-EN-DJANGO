from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from clientes.models import Cliente

@login_required
def index(request):
    # Obtener el cliente asociado con el usuario logueado
    cliente = Cliente.objects.get(user=request.user)

    # Pasar el cliente a la plantilla
    return render(request, 'homebanking/homebanking.html', {'cliente': cliente})
