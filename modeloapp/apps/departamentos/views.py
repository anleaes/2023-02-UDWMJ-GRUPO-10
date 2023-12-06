from django.shortcuts import render, get_object_or_404, redirect
from .forms import DepartamentoForm
from .models import Departamento

# Create your views here.

def add_departamento(request):
    template_name = 'departamentos/add_departamento.html'
    context = {}
    if request.method == 'POST':
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('departamentos:list_departamentos')
    form = DepartamentoForm()
    context['form'] = form
    return render(request, template_name, context)

def list_departamentos(request):
    template_name = 'departamentos/list_departamentos.html'
    departamentos = Departamento.objects.filter()
    context = {
        'departamentos': departamentos
    }
    return render(request, template_name, context)

def edit_departamento(request, id_departamento):
    template_name = 'departamentos/add_departamento.html'
    context ={}
    departamento = get_object_or_404(Departamento, id=id_departamento)
    if request.method == 'POST':
        form = DepartamentoForm(request.POST, instance=departamento)
        if form.is_valid():
            form.save()
            return redirect('departamentos:list_departamentos')
    form = DepartamentoForm(instance=departamento)
    context['form'] = form
    return render(request, template_name, context)

def delete_departamento(request, id_departamento):
    departamento = Departamento.objects.get(id=id_departamento)
    departamento.delete()
    return redirect('departamentos:list_departamentos')