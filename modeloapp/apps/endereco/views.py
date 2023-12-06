from django.shortcuts import render
from .forms import EnderecoForm

# Create your views here.

def endereco_view(request):
    if request.method == 'POST':
        form = EnderecoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = EnderecoForm()
    return render(request, 'endereco.html', {'form': form})