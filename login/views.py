from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm

def registro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Inicia sesión automáticamente después de registrar
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
            return redirect('/homebanking')  # Redirige a la página principal
        else:
            return render(request, 'login/login.html', {'form': form, 'error': 'Credenciales inválidas'})
    else:
        form = AuthenticationForm()

    return render(request, 'login/login.html', {'form': form})
def logout_view(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect('login:login')  # Redirige al login
