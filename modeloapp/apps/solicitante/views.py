from django.shortcuts import render, redirect
from .forms import SolicitanteForm

# Create your views here.

def add_solicitante(request):
    if request.method == 'POST':
        form = SolicitanteForm(request.POST)
        if form.is_valid():
            solicitante = form.save()
            return redirect(request.GET.get('next', '/'))
    else:
        form = SolicitanteForm()

    return redirect(request, 'add_solicitante.html', {'form': form})