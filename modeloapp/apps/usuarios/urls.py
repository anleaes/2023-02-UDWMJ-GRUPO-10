from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('novo-usuario/',views.add_user, name='add_user'),
]
