from django.db.utils import IntegrityError
from django.shortcuts import render,redirect
from .models import User
from django.views import View
from django.urls import reverse
from django.http import HttpResponse,HttpRequest
from django.contrib import auth
from django.contrib import messages
from django.contrib.messages import constants

class RegisterView(View):
    template_name: str = "registration/cadastro.html" 
    def get(self,request:HttpRequest) -> HttpResponse:    
        return render(request,self.template_name)
    def post(self,request:HttpRequest) -> HttpResponse:
        
        username: str = request.POST.get('name')
        email: str = request.POST.get('email')
        password: str = request.POST.get('password')
        confirm_password: str = request.POST.get('repeat_password')
        telefone: str  = request.POST.get('telefone')
            
        users = User.objects.filter(username=username,email=email)

        if users.exists():
            messages.add_message(request,constants.ERROR,'Usuário já existente')
            return redirect(reverse('register'))
        try:
            users=User.objects.create_user(username=username,email=email,password=confirm_password, telefone=telefone)
            messages.add_message(request,constants.SUCCESS,'Usuário criado com sucesso')
            
            return redirect(reverse('login'))
            
        except IntegrityError:
            messages.add_message(request, constants.ERROR,f'Erro interno no servidor {IntegrityError}')
            return redirect(reverse('register')) 

class LoginView(View):      

    template_name: str = "registration/login.html" 

    def get(self,request:HttpRequest) -> HttpResponse:    
        return render(request,self.template_name)
    def post(self,request:HttpRequest) ->HttpResponse:
    
        username:str = request.POST.get('name')
        password:str = request.POST.get('password')
        
        
        users =auth.authenticate(request,username=username,password=password)
        
        if users:
            auth.login(request,users)
            return redirect(reverse('home'))    
        messages.add_message(request,constants.ERROR,'Username ou senha inválidos')
        return redirect(reverse('login'))
class LogoutView(View):

    def get(self,request:HttpRequest) -> HttpResponse:
        auth.logout(request)
        return redirect(reverse('login'))
