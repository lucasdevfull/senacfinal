from django.urls import path
from . import views


urlpatterns = [
    path('register/',views.register, name='cadastro'),
    path('',views.login,name='login'),
]