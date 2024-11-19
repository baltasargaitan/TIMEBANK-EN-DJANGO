
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import RegistroForm

def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Iniciar sesión automáticamente después de registrarse
            return redirect("homebanking:index")  # Redirigir al homebanking
    else:
        form = RegistroForm()

    return render(request, "login/registro.html", {"form": form})
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/homebanking')  # Redirige a la principal
        else:
            return render(request, 'login/login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'login/login.html')

def logout_view(request):
    logout(request)
    return redirect('login:login')
