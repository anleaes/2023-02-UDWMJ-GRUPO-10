from django.shortcuts import render, get_object_or_404, redirect
from .forms import SolicitacaoForm
from .models import Solicitacao, Endereco, SolicitacaoEndereco

# Create your views here.

def add_solicitacao(request):
    template_name = 'solicitacoes/add_solicitacao.html'
    context = {}
    if request.method == 'POST':
        form = SolicitacaoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('solicitacoes:list_solicitacoes')
    form = SolicitacaoForm()
    context['form'] = form
    return render(request, template_name, context)

def list_solicitacoes(request):
    template_name = 'solicitacoes/list_solicitacoes.html'
    solicitacao_endereco = SolicitacaoEndereco.objects.filter()
    endereco = Endereco.objects.filter()
    solicitacao = Solicitacao.objects.filter()
    context = {
        'solicitacao': solicitacao,
        'endereco': endereco,
        'solicitacao_endereco': solicitacao_endereco,
    }
    return render(request, template_name, context)

def edit_solicitacao(request, id_solicitacao):
    template_name = 'solicitacoes/add_solicitacao.html'
    context ={}
    solicitacao = get_object_or_404(Solicitacao, id=id_solicitacao)
    if request.method == 'POST':
        form = SolicitacaoForm(request.POST, instance=solicitacao)
        if form.is_valid():
            form.save()
            return redirect('solicitacoes:list_solicitacoes')
    form = SolicitacaoForm(instance=solicitacao)
    context['form'] = form
    return render(request, template_name, context)

def delete_solicitacao(request, id_solicitacao):
    solicitacao = Solicitacao.objects.get(id=id_solicitacao)
    solicitacao.delete()
    return redirect('solicitacoes:list_solicitacoes')