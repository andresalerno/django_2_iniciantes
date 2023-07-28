"""
Definição das URLs para a aplicação

URL configuration for produtos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from items.views import home, produtos, clientes, create_produto # aula 17 # aula 22 create_produto

urlpatterns = [
    path('admin/', admin.site.urls),
    # aula 17: linhas 26 a 28
    path('home/', home, name="home"), # aula 24: adicionando um nome para a home
    path('produtos/', produtos),
    path('clientes/', clientes),
    path('create_produto/', create_produto),
]
