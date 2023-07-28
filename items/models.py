from django.db import models

# Create your models here.
# Aula 13 => etapa 1: linhas 5 a 8
class Produto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    descricao = models.TextField()
#Aula 14: definimos aqui esse método para aparecer o nome na lista de produtos
    def __str__(self):
        return self.nome
    