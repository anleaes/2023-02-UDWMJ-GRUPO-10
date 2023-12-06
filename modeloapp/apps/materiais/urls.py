from django.urls import path
from . import views

app_name = 'materiais'

urlpatterns = [
    path('lista_materiais/', views.lista_materiais, name='lista_materiais'),
    path('adiciona_material/', views.adiciona_material, name='adiciona_material'),
]