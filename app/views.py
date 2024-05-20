from django.shortcuts import render,redirect
from django.contrib.messages import constants
from django.contrib import messages 
from django.urls import reverse
from django.db import transaction
from .models import Produto
# Create your views here.
def home(request):
    template_name ='home.html'
    return render(request,template_name)

def adicionar_produto(request):
    if request.method == 'GET':
        template_name = 'adicionar_produto.html' 
        return render(request,template_name)
    elif request.method == 'POST':
        produto = request.POST.get('produto')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        fabricante = request.POST.get('fabricante')
        categoria = request.POST.get('categoria')

        with transaction.atomic():
            try:
                produtos=Produto(user = request.user,
                                nome_produto = produto,
                                descricao = descricao,
                                preco = preco,
                                fabricante = fabricante,
                                categoria = categoria
                                )
                produtos.save()
            except:
                messages.add_message(request,constants.ERROR,'Erro ao enviar o cadastro!')
                return redirect(reverse('adicionar_produto'))
        messages.add_message(request,constants.SUCCESS,'Produto salvo com sucesso!')
        return redirect(reverse('home'))