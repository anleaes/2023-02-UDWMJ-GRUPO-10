from django.shortcuts import render, redirect
from .forms import SolicitanteForm
from .models import Solicitante

# Create your views here.

def add_solicitante(request):
    template_name = 'solicitante/add_solicitante.html'
    context = {}
    if request.method == 'POST':
        form = SolicitanteForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('solicitante:add_solicitante')
    form = SolicitanteForm()
    context['form'] = form
    return render(request, template_name, context)

def list_solicitantes(request):
    template_name = 'solicitante/list_solicitantes.html'
    cpf = Solicitante.objects.filter()
    context = {
        'cpf': cpf,
    }
    return render(request, template_name, context)

def delete_solicitante(request, id_solicitante):
    solicitante = Solicitante.objects.get(id=id_solicitante)
    solicitante.delete()
    return redirect('solicitante:list_solicitantes')