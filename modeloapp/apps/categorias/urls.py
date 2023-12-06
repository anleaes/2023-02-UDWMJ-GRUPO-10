from django.urls import path
from . import views

app_name = 'categorias'

urlpatterns = [
    path('', views.list_categorias, name='list_categorias'),
    path('adicionar/', views.add_categoria, name='add_categoria'),
    path('editar/<int:id_category>/', views.edit_categoria, name='edit_categoria'),
    path('excluir/<int:id_category>/', views.delete_categoria, name='delete_categoria'),
]