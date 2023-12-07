from django.urls import path
from . import views

app_name = 'solicitacoes'

urlpatterns = [
    path('', views.list_solicitacoes, name='list_solicitacoes'),
    path('adicionar/', views.add_solicitacao, name='add_solicitacao'),
    path('excluir/<int:id_solicitacao>/', views.delete_solicitacao, name='delete_solicitacao'),
]
