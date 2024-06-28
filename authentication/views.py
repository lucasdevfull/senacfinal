from django.db.utils import IntegrityError
from django.shortcuts import render, redirect
from .models import User
from django.views import View
from django.urls import reverse,reverse_lazy
from django.http import HttpResponse,HttpRequest
from django.contrib import auth
from django.contrib import messages
from django.contrib.messages import constants
from backend.mixin import GetMixin

class RegisterView(GetMixin,View):
    template_name: str = "registration/cadastro.html"
    success_url = reverse_lazy('login')
    register_url = reverse_lazy('register')
    def get_success_url(self, url):
        return super().get_success_url(url)

    def get(self, request:HttpRequest) -> HttpResponse:
        return render(request, self.template_name)
    def post(self, request:HttpRequest) -> HttpResponse:
        
        username: str = request.POST.get('name')
        email: str = request.POST.get('email')
        password: str = request.POST.get('password')
        confirm_password: str = request.POST.get('repeat_password')
        telefone: str  = request.POST.get('telefone')
            
        users = User.objects.filter(username=username,email=email)

        success_url = self.get_success_url(self.success_url)

        redirect_url = super().get_redirect_url(self.register_url)

        if users.exists():
            
            messages.add_message(request,constants.ERROR,'Usuário já existente')
            return redirect(redirect_url)
        try:
            users=User.objects.create_user(username=username,email=email,password=confirm_password, telefone=telefone)
            messages.add_message(request,constants.SUCCESS,'Usuário criado com sucesso')
            
            return redirect(success_url)
            
        except IntegrityError:
            messages.add_message(request, constants.ERROR,f'Erro interno no servidor {IntegrityError}')
            return redirect(redirect_url) 

class LoginView(GetMixin,View):      

    template_name: str = "registration/login.html" 
    success_url = reverse_lazy('listar')
    login_url = reverse_lazy('login')
    def get_success_url(self, url):
        return super().get_success_url(url)
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name)
    def post(self, request: HttpRequest) -> HttpResponse:

        username:str = request.POST.get('name')
        password:str = request.POST.get('password')
        
        users = auth.authenticate(request,username=username,password=password)
        
        success_url=self.get_success_url(self.success_url)
        
        login_url=self.get_redirect_url(self.login_url)
        
        if users:
            auth.login(request, users)
            return redirect(success_url)
        messages.add_message(request,constants.ERROR,'Username ou senha inválidos')
        return redirect(login_url)
class LogoutView(GetMixin,View):
    redirect_url = reverse_lazy('login')

    def get_redirect_url(self, url):
        return super().get_redirect_url(url)
    
    def get(self, request: HttpRequest) -> HttpResponse:
        auth.logout(request)
        url=self.get_redirect_url(self.redirect_url)
        return redirect(url)


