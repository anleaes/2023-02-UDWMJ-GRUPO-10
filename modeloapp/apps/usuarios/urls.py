from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('novo-usuario/',views.add_user, name='add_user'),
    path('',views.user_login, name='user_login'),
    path('sair/',views.user_logout, name='user_logout'),
    path('alterar-senha/',views.user_change_password, name='user_change_password'),
    path('alterar-usuario/<username>/',views.user_change_information, name='user_change_information'),
]
