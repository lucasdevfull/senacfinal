from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.HomeView.as_view(), name='home'),
    path('adicionar_produto/',views.ProdutoView.as_view(), name='adicionar'),
    path('listar_produto/',views.ProdutoListView.as_view(), name = 'listar'),
    path('details_produto/<int:id>/',views.ProdutoDetailsView.as_view(), name='detalhe'),
    path('editar_produto/<int:id>/',views.ProdutoUpdateView.as_view(), name = 'editar'),
    path('deletar_produto/<int:id>/',views.ProdutoDeleteView.as_view(), name = 'deletar'),
    path('adicionar_categoria/',views.CategoriaView.as_view(), name='categoria'),
    path('adicionar_fabricante/',views.FabricanteView.as_view(), name='fabricante')
]