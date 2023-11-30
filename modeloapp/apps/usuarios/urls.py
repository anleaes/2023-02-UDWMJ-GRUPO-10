from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.list_usuarios, name='list_usuarios'),
    path('adicionar/', views.add_usuarios, name='add_usuarios'),
    path('editar/<int:id_usuario>/', views.edit_usuario, name='edit_usuario'),
    path('excluir/<int:id_usuario>/', views.delete_usuario, name='delete_usuario'),
]
