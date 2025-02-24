from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm

#Vista para registrar un nuevo usuario
def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('lista_denuncias')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registro.html', {'form': form})

# Vista para autenticar a los usuarios
def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('lista_denuncias')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Vista para cerrar sesion
@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('login')

