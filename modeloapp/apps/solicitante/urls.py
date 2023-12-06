from django.urls import path
from . import views

app_name = 'solicitante'

urlpatterns = [
    path('solicitante/', views.add_solicitante, name='add_solicitante'),
]