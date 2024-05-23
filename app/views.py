from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.messages import constants
from django.contrib import messages 
from django.urls import reverse
from django.db import transaction
from .models import Produto
# Create your views here.
def home(request):
    template_name ='home.html'
    return render(request,template_name)

def listar_produto(request):
    if request.method == 'GET':
        produto = Produto.objects.all()
        template_name = 'produtos/listar_produto.html'
        context = {'produto':produto}
        return render(request,template_name,context)

def adicionar_produto(request):
    if request.method == 'GET':
        template_name = 'adicionar_produto.html' 
        return render(request,template_name)
    elif request.method == 'POST':
        nome_produto = request.POST.get('produto')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        fabricante = request.POST.get('fabricante')
        categoria = request.POST.get('categoria')

        with transaction.atomic():
            try:
                produtos=Produto(user = request.user,
                                nome_produto = nome_produto,
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

def editar_produto(request,produto_id):
    produto = get_object_or_404(Produto,id=produto_id)
    template_name = 'produtos/editar_produto.html'
    context = {'produto':produto}
    if request.method == 'POST':
        produto.nome_produto = request.POST.get('produto')
        produto.descricao = request.POST.get('descricao')
        produto.preco = request.POST.get('preco')
        produto.fabricante = request.POST.get('fabricante')
        produto.categoria = request.POST.get('categoria')
        produto.save()
        return redirect(reverse('home'))
    return render(request,template_name,context)

def deletar_produto(request, produto_id):
    produto = get_object_or_404(Produto,id=produto_id)
    template_name = 'produtos/deletar_produtos.html'
    context = {'produto':produto}
    if request.method == 'POST':
        produto.delete()
        return redirect(reverse('home'))
    return render(request,template_name,context)