from django.shortcuts import render, redirect

# Create your views here.

from .forms import MateriaisForm

def lista_materiais(request):
    materiais = MateriaisForm.objects.all()
    return render(request, 'materiais/lista_materiais.html', {'materiais': materiais})

def adiciona_material(request):
    if request.method == 'POST':
        form = MateriaisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_materiais')
    else:
        form = MateriaisForm()
    return render(request, 'materiais/adiciona_material.html', {'form': form})
