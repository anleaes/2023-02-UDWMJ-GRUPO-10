from django.urls import path
from .views import registrar, entrar, sair, dashboard, modificar_informacoes

app_name = 'usuarios'

urlpatterns = [
    path('registrar/', registrar, name='registrar'),
    path('entrar/', entrar, name='entrar'),
    path('sair/', sair, name='sair'),
    path('dashboard/', dashboard, name='dashboard'),
    path('modificar_informacoes/', modificar_informacoes, name='modificar_informacoes'),
]