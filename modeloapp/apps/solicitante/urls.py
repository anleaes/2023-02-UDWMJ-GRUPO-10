from django.urls import path
from . import views

app_name = 'solicitante'

urlpatterns = [
    path('solicitante/', views.list_solicitantes, name='list_solicitantes'),
    path('adicionar/', views.add_solicitante, name='add_solicitante'),
    path('editar/<int:id_solicitante>/', views.edit_solicitante, name='edit_solicitante'),
    path('excluir/<int:id_solicitante>/', views.delete_solicitante, name='delete_solicitante'),
]