from django.urls import path
from . import views

app_name = 'solicitante'

urlpatterns = [
    path('add_solicitante/', views.add_solicitante, name='add_solicitante'),
]