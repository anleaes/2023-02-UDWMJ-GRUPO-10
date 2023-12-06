from django.shortcuts import render, redirect
from .forms import EnderecoForm

# Create your views here.

def add_endereco(request):
    template_name = 'endereco/add_endereco.html'
    context = {}
    if request.method == 'POST':
        form = EnderecoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('endereco:add_endereco')
    form = EnderecoForm()
    context['form'] = form
    return render(request, template_name, context)