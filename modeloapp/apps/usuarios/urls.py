from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.list_usuarios, name='list_usuarios'),
    path('adicionar/', views.add_usuarios, name='add_usuarios'),
    path('editar/<int:id_usuarios>/', views.edit_usuarios, name='edit_usuarios'),
    path('excluir/<int:id_usuarios>/', views.delete_usuarios, name='delete_usuarios'),
]
