from django.urls import path, include
from . import views

app_name = 'atendimento'

urlpatterns = [
    path('add/', views.add_atendimento, name='add_atendimento'),
    path('excluir/<int:id_atendimento>/', views.delete_atendimento, name='delete_atendimento'),
]