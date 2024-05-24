from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.home, name='home'),
    path('adicionar_produto',views.adicionar_produto, name='adicionar'),
    path('listar_produto',views.listar_produto, name = 'listar'),
    path('editar_produto/<int:produto_id>',views.editar_produto, name = 'editar'),
    path('deletar_produto/<int:produto_id>',views.deletar_produto, name = 'deletar'),
]