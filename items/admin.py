from django.contrib import admin
from .models import Produto

# Register your models here.
# Aula 13 => para registrar a nossa model no admin precisamos adiciona-la aqui. Etapa 2: linha 2 e 6 
admin.site.register(Produto)
