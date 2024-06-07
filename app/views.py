from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import permission_required,login_required
from django.contrib.messages import constants
from django.contrib import messages 
from django.urls import reverse
from django.db import transaction,IntegrityError
from .models import Produto,Categoria,Fabricante
# Create your views here.
def home(request):
    template_name ='products/home.html'
    return render(request,template_name)

def listar_produto(request):
    if request.method == 'GET':
        fabricante= request.GET.get('fabricante')
        categoria = request.GET.get('categoria')
        produtos = Produto.objects.all()

        todos_produtos = []
        if categoria:
            categoria_id = Categoria.objects.filter(pk=int(categoria)).first().pk
            for produto in produtos:
                if produto.categoria.pk == categoria_id:
                    todos_produtos.append(produto)
        
        if fabricante:
            fabricante_id=Fabricante.objects.filter(pk=int(fabricante)).first().pk
            for produto in produtos:
                if produto.fabricante.pk == fabricante_id:
                    todos_produtos.append(produto)

        template_name = 'products/listar_produto.html'

        context = {
            'produtos': todos_produtos if categoria else produtos,
            'categorias': Categoria.objects.all(),
            'fabricante': Fabricante.objects.all()
        }
        return render(request,template_name,context)

def adicionar_categoria(request):
    if request.method =='POST':
        categoria=request.POST.get('categoria')
        
        categoria=Categoria(nome=categoria)

        categoria.save()
        return redirect(reverse('adicionar'))
    template_name = 'products/adicionar_categoria.html' 
    return render(request,template_name)

def adicionar_fabricante(request):
    if request.method =='POST':
        fabricante=request.POST.get('fabricante')
        
        fabricante=Fabricante(nome=fabricante)

        fabricante.save()
        return redirect(reverse('adicionar'))
    template_name = 'products/adicionar_fabricante.html' 
    return render(request,template_name)
    
def adicionar_produto(request):
    if request.method == 'GET':
        fabricante = Fabricante.objects.all()
        categoria = Categoria.objects.all()
        context = {'fabricante':fabricante,
                   'categorias':categoria}
        template_name = 'products/adicionar_produto.html' 
        return render(request,template_name,context)
    elif request.method == 'POST':
        nome_produto = request.POST.get('nome_produto')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        quantidade = request.POST.get('quantidade') 
        fabricante_id = request.POST.get('fabricante')
        categoria_id = request.POST.get('categoria')

        
        with transaction.atomic():
            try:
                fabricante = Fabricante.objects.get(id=fabricante_id)
                categoria = Categoria.objects.get(id=categoria_id)
                
                produto = Produto(
                    user=request.user,
                    nome_produto=nome_produto,
                    descricao=descricao,
                    preco=preco,
                    estoque=quantidade,
                    fabricante=fabricante,
                    categoria=categoria
                )
                produto.save()
                messages.add_message(request,constants.SUCCESS,'Produto salvo com sucesso!')
                return redirect(reverse('home'))
            except Exception as e:
                print(str(e))
                messages.add_message(request,constants.ERROR,f'Erro ao enviar o cadastro. motivo{e}')
                return redirect(reverse('adicionar'))
            
            

def details_produto(request,produto_id):
    if request.user_hasperm:
        produto = get_object_or_404(Produto,id=produto_id)
        template_name = 'products/details_produto.html'
        context = {'produto':produto}
        return render(request,template_name,context)

def editar_produto(request,produto_id):
    produto = get_object_or_404(Produto,id=produto_id)
    template_name = 'products/editar_produto.html'
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
    template_name = 'products/deletar_produtos.html'
    context = {'produto':produto}
    if request.method == 'POST':
        produto.delete()
        return redirect(reverse('home'))
    return render(request,template_name,context)