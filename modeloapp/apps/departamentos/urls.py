from django.urls import path
from . import views

app_name = 'departamentos'

urlpatterns = [
    path('', views.list_departamentos, name='list_departamentos'),
    path('adicionar/', views.add_departamento, name='add_departamento'),
    path('editar/<int:id_departamentos>/', views.edit_departamento, name='edit_departamento'),
    path('excluir/<int:id_departamentos>/', views.delete_departamento, name='delete_departamento'),
]
