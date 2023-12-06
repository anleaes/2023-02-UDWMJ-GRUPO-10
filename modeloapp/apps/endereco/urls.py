from django.urls import path
from . import views

app_name = 'endereco'

urlpatterns = [
    path('endereco/', views.add_endereco, name='endereco'),
]