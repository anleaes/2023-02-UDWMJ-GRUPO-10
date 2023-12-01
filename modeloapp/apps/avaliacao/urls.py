from . import views
from django.urls import path, include

app_name = 'avaliacao'

urlpatterns = [
    path('avaliacao/',views.add_avaliacao, name='add_avaliacao'),
]