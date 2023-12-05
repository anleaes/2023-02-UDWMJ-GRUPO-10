from django.shortcuts import render, get_object_or_404, redirect
from .forms import ServicoForm
from .models import Servico


# Create your views here.

def add_servico(request):
    template_name = 'servicos/add_servico.html'
    context = {}
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('servicos:list_servicos')
    form = ServicoForm()
    context['form'] = form
    return render(request, template_name, context)

def list_servicos(request):
    template_name = 'servicos/list_servicos.html'
    servicos = Servico.objects.filter()
    context = {
        'servicos': servicos,
    }
    return render(request, template_name, context)

def edit_servicos(request, id_servico):
    template_name = 'servicos/add_servico.html'
    context ={}
    servico = get_object_or_404(Servico, id=id_servico)
    if request.method == 'POST':
        form = ServicoForm(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            return redirect('servicos:list_servicos')
    form = ServicoForm(instance=servico)
    context['form'] = form
    return render(request, template_name, context)

def delete_servico(request, id_servico):
    servico = Servico.objects.get(id=id_servico)
    servico.delete()
    return redirect('servicos:list_servicos')