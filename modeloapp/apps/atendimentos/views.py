from django.shortcuts import render, get_object_or_404, redirect
from .forms import AtendimentoForm
from .models import Atendimento, Solicitacao
# Create your views here.

def add_atendimento(request):
    template_name = 'atendimento/add_atendimento.html'
    context = {}
    if request.method == 'POST':
        form = AtendimentoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('atendimentos:list_atendimentos')
    form = AtendimentoForm()
    context['form'] = form
    return render(request, template_name, context)

def list_atendimentos(request):
    template_name = 'atendimentos/list_atendimentos.html'
    id_solicitacao= Solicitacao.objects.filter()
    data = Atendimento.objects.filter()
    hora = Atendimento.objects.filter()
    departamento = Atendimento.objects.filter()
    rua = Atendimento.objects.filter()
    numero = Atendimento.objects.filter()
    bairro = Atendimento.objects.filter()
    complemento = Atendimento.objects.filter()
    context = {
        'id_solicitacao': id_solicitacao,
        'data': data,
        'hora': hora,
        'departamento': departamento,
        'rua': rua,
        'numero': numero,
        'bairro': bairro,
        'complemento': complemento,
    }
    return render(request, template_name, context)

def edit_atendimento(request, id_atendimento):
    template_name = 'atendimentos/add_atendimento.html'
    context ={}
    atendimento = get_object_or_404(Atendimento, id=id_atendimento)
    if request.method == 'POST':
        form = AtendimentoForm(request.POST, instance=atendimento)
        if form.is_valid():
            form.save()
            return redirect('atendimentos:list_atendimento')
    form = AtendimentoForm(instance=atendimento)
    context['form'] = form
    return render(request, template_name, context)

def delete_atendimento(request, id_atendimento):
    atendimento = Atendimento.objects.get(id=id_atendimento)
    atendimento.delete()
    return redirect('atendimentos:list_atendimentos')