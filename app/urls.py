from django.urls import path
from . import views
urlpatterns = [
    path('dashboard/',views.home, name='home'),
    path('adicionar_produto',views.adicionar_produto, name='adicionar')
]