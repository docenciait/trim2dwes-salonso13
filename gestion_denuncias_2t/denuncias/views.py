from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Denuncia
from .forms import DenunciaForm

# Vista para crear una nueva denuncia
@login_required
def crear_denuncia(request):
    if request.method == 'POST':
        form = DenunciaForm(request.POST, request.FILES)
        if form.is_valid(): 
            denuncia = form.save(commit=False)
            denuncia.usuario = request.user
            denuncia.save()
            return redirect('lista_denuncias')  # Redirecciona a la lista
    else:
        form = DenunciaForm()  # Crea formulario vacío
    return render(request, 'crear_denuncia.html', {'form': form})

# Vista para listar todas las denuncias
@login_required
def lista_denuncias(request):
    # Obtiene todas las denuncias ordenadas por fecha de creación (más recientes primero)
    denuncias = Denuncia.objects.all().order_by('-fecha_creacion')
    return render(request, 'lista_denuncias.html', {'denuncias': denuncias})

# Vista para editar una denuncia existente
@login_required
def editar_denuncia(request, id):
    # Obtiene la denuncia o devuelve nada si no existe o no pertenece al usuario
    denuncia = get_object_or_404(Denuncia, id=id, usuario=request.user)
    if request.method == 'POST':
        # Crea un formulario con datos POST, archivos y la instancia actual
        form = DenunciaForm(request.POST, request.FILES, instance=denuncia)
        if form.is_valid():
            form.save()
            return redirect('lista_denuncias')
    else:
        form = DenunciaForm(instance=denuncia)
    return render(request, 'editar_denuncia.html', {'form': form})

# Vista para eliminar una denuncia
@login_required
def eliminar_denuncia(request, id):
    # Obtiene la denuncia o devuelve nada si no existe o no pertenece al usuario
    denuncia = get_object_or_404(Denuncia, id=id, usuario=request.user)
    if request.method == 'POST':  # Si se confirma la eliminación eliminara la denuncia
        denuncia.delete()
        return redirect('lista_denuncias')
    return render(request, 'eliminar_denuncia.html', {'denuncia': denuncia})