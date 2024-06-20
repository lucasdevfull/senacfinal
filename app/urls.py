from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.HomeView.as_view(), name='home'),
    path('adicionar_produto/',views.ProdutoView.as_view(), name='adicionar'),
    path('listar_produto/',views.ProdutoListView.as_view(), name = 'listar'),
    path('details_produto/<int:id>/',views.details_produto, name='detalhe'),
    path('editar_produto/<int:id>/',views.editar_produto, name = 'editar'),
    path('deletar_produto/<int:id>/',views.deletar_produto, name = 'deletar'),
    path('adicionar_categoria/',views.CategoriaView.as_view(), name='categoria'),
    path('adicionar_fabricante/',views.FabricanteView.as_view(), name='fabricante')
]