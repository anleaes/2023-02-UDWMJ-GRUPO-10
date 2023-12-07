from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UsuarioCreationForm, UsuarioChangeForm

def registrar(request):
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('login')
    else:
        form = UsuarioCreationForm()
    return render(request, 'registrar.html', {'form': form})

def entrar(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        user = authenticate(request, email=email, senha=senha)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login bem-sucedido!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Credenciais inválidas. Tente novamente.')
    return render(request, 'entrar.html')

@login_required
def sair(request):
    logout(request)
    messages.success(request, 'Logout bem-sucedido!')
    return redirect('login')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def modificar_informacoes(request):
    if request.method == 'POST':
        form = UsuarioChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Informações do usuário modificadas com sucesso!')
            return redirect('dashboard')
    else:
        form = UsuarioChangeForm(instance=request.user)
    return render(request, 'modificar_informacoes.html', {'form': form})