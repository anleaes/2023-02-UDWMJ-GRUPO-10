from django.shortcuts import render, get_object_or_404, redirect
from .forms import UsuariosForm, LogoutForm
from .models import Usuarios, Solicitante, UsuariosSolicitante

def logout(request):
    if request.method == 'POST':
        form = LogoutForm(request.POST)
        if form.is_valid():
            request.session.flush()
            return redirect('index')
    else:
        form = LogoutForm()
    return render(request, 'logout.html', {'form': form})

def add_usuarios(request):
    template_name = 'usuarios/add_usuarios.html'
    context = {}
    if request.method == 'POST':
        form = UsuariosForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('usuarios:list_usuarios')
    form = UsuariosForm()
    context['form'] = form
    return render(request, template_name, context)

def list_usuarios(request):
    template_name = 'usuarios/list_usuarios.html'
    usuarios_solicitante = UsuariosSolicitante.objects.filter()
    solicitante = Solicitante.objects.filter()
    usuarios = usuarios.objects.filter()
    context = {
        'usuarios': usuarios,
        'solicitante': solicitante,
        'usuarios_solicitante': usuarios_solicitante
    }
    return render(request, template_name, context)

def edit_usuarios(request, id_usuarios):
    template_name = 'usuarios/add_usuarios.html'
    context ={}
    usuarios = get_object_or_404(usuarios, id=id_usuarios)
    if request.method == 'POST':
        form = UsuariosForm(request.POST, instance=usuarios)
        if form.is_valid():
            form.save()
            return redirect('usuarios:list_usuarios')
    form = UsuariosForm(instance=usuarios)
    context['form'] = form
    return render(request, template_name, context)

def delete_usuarios(request, id_usuarios):
    usuarios = usuarios.objects.get(id=id_usuarios)
    usuarios.delete()
    return redirect('usuarios:list_usuarios')