from django.shortcuts import render, redirect
from .forms import SolicitanteForm

# Create your views here.

def fazer_solicitacao(request):
    if request.method == 'POST':
        form = SolicitanteForm(request.POST)
        if form.is_valid():
            solicitante = form.save()
            return redirect(request, 'sucesso.html', {'mensagem': 'Solicitação feita com sucesso!'})
    else:
        form = SolicitanteForm()

    return redirect(request, 'fazer_solicitacao.html', {'form': form})