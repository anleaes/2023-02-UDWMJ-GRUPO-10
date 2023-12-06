from django.urls import path
from .views import fazer_solicitacao

urlpatterns = [
    path('fazer_solicitacao/', fazer_solicitacao, name='fazer_solicitacao'),
]