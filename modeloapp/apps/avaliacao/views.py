from django.shortcuts import render, redirect
from .models import Avaliacao
from .forms import AvaliacaoForm

# Create your views here.

def create_avaliacao(request):
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('avaliacao_list')
    else:
        form = AvaliacaoForm()
    return render(request, 'create_avaliacao.html', {'form': form})