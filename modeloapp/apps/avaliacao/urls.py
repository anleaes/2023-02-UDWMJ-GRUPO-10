from . import views
from django.urls import path, include

app_name = 'avaliacao'

urlpatterns = [
    path('avaliacao/', include('avaliacao.urls')),
]