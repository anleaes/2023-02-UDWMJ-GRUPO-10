from django.shortcuts import render
from .forms import EnderecoForm

# Create your views here.

def add_endereco(request):
    if request.method == 'POST':
        form = EnderecoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = EnderecoForm()
    return render(request, 'add_endereco.html', {'form': form})