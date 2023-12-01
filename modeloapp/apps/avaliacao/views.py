from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .forms import AvaliacaoForm
from .models import AvaliacaoModel

def create_avaliacao(request):
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            nota = form.cleaned_data['nota']
            avaliacao = AvaliacaoModel(nota)
            avaliacao_resultado = avaliacao.avaliar()
            return render(request, 'create_avaliacao.html', {'form': form, 'avaliacao_resultado': avaliacao_resultado})
    else:
        form = AvaliacaoForm()
    return render(request, 'create_avaliacao.html', {'form': form})