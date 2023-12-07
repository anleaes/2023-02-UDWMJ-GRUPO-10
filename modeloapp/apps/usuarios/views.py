from django.shortcuts import render, redirect
from .forms import RegistroForm

# Create your views here.

def add_user(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'add_user.html', {'form': form})
