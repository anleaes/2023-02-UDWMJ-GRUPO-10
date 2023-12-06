from django.shortcuts import render, redirect
from .models import Avaliacao
from .forms import AvaliacaoForm

# Create your views here.

def add_avaliacao(request):
    template_name = 'avaliacao/add_avaliacao.html'
    context = {}
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('avaliacao:add_avaliacao')
    form = AvaliacaoForm()
    context['form'] = form
    return render(request, template_name, context)