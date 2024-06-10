from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home, name='home'),
    path('adicionar_produto/',views.adicionar_produto, name='adicionar'),
    path('listar_produto/',views.listar_produto, name = 'listar'),
    path('details_produto/<int:id>/',views.details_produto, name='detalhe'),
    path('editar_produto/<int:id>/',views.editar_produto, name = 'editar'),
    path('deletar_produto/<int:id>/',views.deletar_produto, name = 'deletar'),
    path('adicionar_categoria/',views.adicionar_categoria, name='categoria'),
    path('adicionar_fabricante/',views.adicionar_fabricante, name='fabricante')
]