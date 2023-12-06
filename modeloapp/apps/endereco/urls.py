from django.urls import path
from . import views

urlpatterns = [
    path('endereco/', views.add_endereco, name='endereco'),
]