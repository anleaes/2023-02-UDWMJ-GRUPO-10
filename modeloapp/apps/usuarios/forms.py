from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Requerido. Informe um endereço de e-mail válido.')

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2')