from django.urls import path
from . import views

app_name = 'departamentos'

urlpatterns = [
    path('', views.list_departamentos, name='list_departamentos'),
    path('adicionar/', views.add_departamentos, name='add_departamentos'),
    path('editar/<int:id_departamentos>/', views.edit_departamentos, name='edit_departamentos'),
    path('excluir/<int:id_departamentos>/', views.delete_departamentos, name='delete_departamentos'),
]
