from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError
import re

def is_password_secure(password):
    # Asegúrate de que la contraseña tenga al menos una mayúscula, un número y un mínimo de 8 caracteres
    if len(password) < 8:
        raise ValidationError("La contraseña debe tener al menos 8 caracteres.")
    if not re.search(r'\d', password):
        raise ValidationError("La contraseña debe contener al menos un número.")
    if not re.search(r'[A-Z]', password):
        raise ValidationError("La contraseña debe contener al menos una letra mayúscula.")
    return password
from clientes.models import Cliente
from cuentas.models import Cuenta
import random
import string

def registro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Inicia sesión automáticamente después de registrar
            
            # Crear el cliente relacionado al usuario
            cliente = Cliente.objects.create(
                user=user,
                nombre=user.first_name,  # Puedes cambiar estos valores según tu formulario
                apellido=user.last_name,
                email=user.email,
                telefono=request.POST['telefono'],
                fecha_nacimiento=request.POST['fecha_nacimiento'],
            )
            
            # Crear una cuenta asociada al cliente recién creado
            # Generar un CVU aleatorio para la cuenta (este es un ejemplo básico)
            cvu = ''.join(random.choices(string.digits, k=22))
            cuenta = Cuenta.objects.create(
                cliente=cliente,
                saldo=100000.0,
                cvu=cvu,
                tipo='CLASSIC'  # O puede ser 'BLACK', 'GOLD', según lo que definas
            )

            return redirect('/homebanking')  # Redirige a la página de inicio
    else:
        form = UserCreationForm()
    return render(request, 'login/registro.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()  # Obtén el usuario de las credenciales
            auth_login(request, user)  # Inicia sesión al usuario
            return redirect(reverse_lazy('homebanking:homebanking'))  # Redirige a la página principal
        else:
            return render(request, 'login/login.html', {'form': form, 'error': 'Credenciales inválidas'})
    else:
        form = AuthenticationForm()

    return render(request, 'login/login.html', {'form': form})

def logout_view(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect('login:login')  # Redirige al login
