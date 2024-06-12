from django.shortcuts import render,redirect
from .models import User
from django.urls import reverse
from django.http import HttpResponse,HttpRequest
from django.contrib import auth
from django.contrib import messages
from django.contrib.messages import constants

# Create your views here.

def register(request:HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        template_name = "registration/cadastro.html"
        return render(request,template_name)
    elif request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('repeat_password')
        telefone = request.POST.get('telefone')
         
        users = User.objects.filter(username=username,email=email)

        if users.exists():
            messages.add_message(request,constants.ERROR,'Usuário já existente')
            return redirect(reverse('register'))
        try:
            users=User.objects.create_user(username=username,email=email,password=confirm_password, telefone=telefone)
            messages.add_message(request,constants.SUCCESS,'Usuário criado com sucesso')
            return redirect(reverse('login'))
        except:
            messages.add_message(request, constants.ERROR,'Erro interno no servidor')
            return redirect(reverse('register')) 
        
def login(request:HttpRequest) -> HttpResponse:
    if request.method == 'GET':
    
        template_name = "registration/login.html"
        return render(request,template_name)
    elif request.method == 'POST':
    
        username = request.POST.get('name')
        password = request.POST.get('password')

        user = User.objects.filter(username=username,password=password)
        if user.exists():
            users =auth.authenticate(request,username=username,password=password)
        else:
            messages.add_message(request,constants.ERROR,'Usuário não existe')
        if users:
            auth.login(request,users)
            return redirect(reverse('home'))
        messages.add_message(request,constants.ERROR,'Username ou senha inválidos')
        return redirect(reverse('login'))

def logout(request):
    auth.logout(request)
    return redirect(reverse('login'))
