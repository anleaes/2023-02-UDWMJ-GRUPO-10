"""modeloapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('contas/', include('usuarios.urls', namespace='usuarios')),
    path('avaliacao/', include('avaliacao.urls', namespace='avaliacao')),
    path('servicos/', include('servicos.urls', namespace='servicos')),
    path('endereco/', include('endereco.urls', namespace='endereco')),
    path('materiais/', include('materiais.urls', namespace='materiais')),
    path('categorias/', include('categorias.urls', namespace='categorias')),
    path('atendimento/', include('atendimento.urls', namespace='atendimento')),
    path('solicitacoes/', include('solicitacoes.urls', namespace='solicitacoes')),
    path('departamentos/', include('deprtamentos.urls', namespace='departamentos')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)