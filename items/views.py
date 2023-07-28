from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto #Aula 20
from .forms import ProdutoForm # Aula 22

# Create your views here.
#recebe uma requisicao e devolve uma resposta
# Aula 16: etapa 1: linhas 7 a 11 (aula 17 etapa 2)
def home(request):
# Aula 18:
    mensagem = 'Mensagem da view'
    produtos = Produto.objects.all() # isso é a mesma coisa que fazer um SLEECT * from Produto
    return render(request, "items/index.html", {"mensagem": mensagem, "produtos": produtos})
    # return HttpResponse('<h1>Área de Home</h1>')

def produtos(request):
    return HttpResponse('<h1>Área de produtos</h1>')

def clientes(request):
    return HttpResponse('<h1>Área de clientes</h1>')

# Aula 22
def create_produto(request):
    form = ProdutoForm(request.POST) # se estamos enviando informações no formulario
    if form.is_valid():
        obj = form.save()
        obj.save() # salva informações no formulário
        form = ProdutoForm() # aula 24 minuto 5,55 para instanciar novamente o formulario apos uma insercao 
    
    return render(request, "items/create_produto.html", {'form': form})
