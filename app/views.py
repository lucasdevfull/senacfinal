import json
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import constants
from django.contrib import messages
from django.views import View

from django.db import transaction,IntegrityError
from django.http import JsonResponse,HttpRequest,HttpResponse
from authentication.models import User
from rolepermissions.roles import assign_role
from rolepermissions.permissions import revoke_permission
from .models import Produto,Categoria,Fabricante
from backend.shortcuts import redirect_url
# Create your views here.

class HomeView(LoginRequiredMixin,View):

    template_name ='products/home.html'
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request,self.template_name)

class ProdutoListView(LoginRequiredMixin,View):

    template_name = 'products/listar_produto.html'
    def get(self, request: HttpRequest) -> HttpResponse:

        fabricante = request.GET.get('fabricante')
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
        user = User.objects.get(id=1)
        assign_role(user, "change")
        revoke_permission(user, "change_product")

        context = {
                'produtos': todos_produtos if categoria or fabricante  else produtos,
                'categorias': Categoria.objects.all(),
                'fabricantes': Fabricante.objects.all()
        }
        return render(request,self.template_name,context)


class CategoriaView(LoginRequiredMixin,View):

    # def post(self,request:HttpRequest) -> JsonResponse:
    def post(self, request):
        try:
            data = json.loads(request.body)
            categoria = Categoria.objects.create(nome=data.get('categoria'))
            context = {
                'nome': categoria.nome,
                'id': categoria.id  
            }

            return JsonResponse({"success": "Categoria cadastrada com sucesso!", "categoria": context})
        except json.JSONDecodeError as e:
            messages.add_message(request,constants.ERROR, f'Erro ao enviar o cadastro. motivo {e}')
            return JsonResponse({"error"})



class FabricanteView(LoginRequiredMixin,View):

    def post(self,request:HttpRequest) -> JsonResponse:
        try:
            data = json.loads(request.body)
            fabricante=Fabricante.objects.create(nome=data.get('fabricante'))
            context = {
                'nome': fabricante.nome,
                'id': fabricante.id
            }
            return JsonResponse({'message':'Fabricante adicionado com sucesso!','fabricante': context})
        except json.JSONDecodeError as e:
            messages.add_message(request,constants.ERROR,f'Erro ao enviar o cadastro. motivo {e}')
            return JsonResponse({"error"})



class ProdutoView(LoginRequiredMixin,View):
    template_name = 'products/adicionar_produto.html'
    
    def get(self,request:HttpRequest) -> HttpResponse:
        fabricante = Fabricante.objects.all()
        categoria = Categoria.objects.all()
        context = {'fabricante':fabricante,
                    'categorias':categoria}
        return render(request,self.template_name,context)

    def post(self,request:HttpRequest) -> HttpResponse:

        nome_produto = request.POST.get('nome_produto')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        quantidade = request.POST.get('quantidade')
        fabricante = request.POST.get('fabricante_produto')
        categoria = request.POST.get('categoria_produto')

        if Produto.objects.filter(nome_produto=nome_produto).exists():
            messages.add_message(request,constants.ERROR,'Produto já existente')
            return redirect_url('adicionar')
        with transaction.atomic():
            try:
                fabricante = Fabricante.objects.get(pk=fabricante)
                categoria = Categoria.objects.get(pk=categoria)

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
                return redirect_url('listar')
            except IntegrityError as e:
                print(str(e))
                messages.add_message(request,constants.ERROR,f'Erro ao enviar o cadastro. motivo {e}')
                return redirect_url('adicionar')



class ProdutoDetailsView(LoginRequiredMixin,View):

     
    template_name = 'products/details_produto.html'
    def get(self,request:HttpRequest,id) -> JsonResponse:

        produto = get_object_or_404(Produto,id=id)

        produto_dict = {
            'id':str(produto.id),
            'nome_produto': str(produto.nome_produto),
            'descricao': str(produto.descricao),
            'preco': str(produto.preco),
            'estoque': str(produto.estoque),
            'fabricante': str(produto.fabricante),
            'categoria': str(produto.categoria),
        }
        # Converte o dicionário em uma string JSON
        produto_serializer = json.dumps(produto_dict)

        if produto:
            return render(request,self.template_name,{'produto':produto})
            #return JsonResponse({"message": "success", "produto": produto_serializer})
        return JsonResponse({"message": "error"})

class ProdutoUpdateView(LoginRequiredMixin,View):
    
    template_name = 'products/editar_produto.html'
    
    def get(self,request:HttpRequest,id) -> HttpResponse:
        produto = get_object_or_404(Produto,id=id)

        context = {'produto':produto,
                    'fabricantes': Fabricante.objects.all(),
                    'categorias': Categoria.objects.all()}
        return render(request,self.template_name,context)

    def post(self,request:HttpRequest,id) -> HttpResponse:

        produto = get_object_or_404(Produto,id=id)
        produto.nome_produto = request.POST.get('nome_produto')
        produto.descricao = request.POST.get('descricao')
        produto.estoque = request.POST.get('quantidade')
        preco =  request.POST.get('preco')
        fabricante = request.POST.get('fabricante')
        categoria = request.POST.get('categoria')

        produto.preco = float(preco.replace(',','.'))
        if fabricante is not None:
            fabricante = get_object_or_404(Fabricante, nome=fabricante)
            produto.fabricante = fabricante
        if categoria is not None:
            categoria = get_object_or_404(Categoria, nome=categoria)
            produto.categoria = categoria
        produto.save()
        messages.add_message(request,constants.SUCCESS,'Atualizado com sucesso')
        return redirect_url('listar')

class ProdutoDeleteView(LoginRequiredMixin,View):

    def get(self,request:HttpRequest,id) -> HttpResponse:
        produto = get_object_or_404(Produto,id=id)
        produto.delete()
        messages.add_message(request,constants.SUCCESS,'Deletado com sucesso')
        return redirect_url('listar')


