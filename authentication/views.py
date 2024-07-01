from django.db.utils import IntegrityError
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse,reverse_lazy
from django.http import HttpResponse,HttpRequest
from django.contrib import auth
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.views import RedirectURLMixin
from django.contrib.auth import get_user_model
from backend.shortcuts import redirect_url
User= get_user_model()
class RegisterView(RedirectURLMixin,View):
    template_name: str = "registration/cadastro.html"

    def get(self, request:HttpRequest) -> HttpResponse:
        return render(request, self.template_name)
    def post(self, request:HttpRequest) -> HttpResponse:
        
        username: str = request.POST.get('name')
        email: str = request.POST.get('email')
        password: str = request.POST.get('password')
        confirm_password: str = request.POST.get('repeat_password')
        telefone: str  = request.POST.get('telefone')
            
        users = User.objects.filter(username=username,email=email)

        if users.exists():
            
            messages.add_message(request,constants.ERROR,'Usuário já existente')
            return redirect_url('register')
        try:
            users=User.objects.create_user(username=username,email=email,password=confirm_password, telefone=telefone)
            messages.add_message(request,constants.SUCCESS,'Usuário criado com sucesso')
            
            return redirect_url('login')
            
        except IntegrityError:
            messages.add_message(request, constants.ERROR,f'Erro interno no servidor {IntegrityError}')
            return redirect_url('register') 

class LoginView(View):      

    template_name: str = "registration/login.html" 
    def get(self, request: HttpRequest) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect(reverse_lazy('listar'))
        return render(request, self.template_name)
    def post(self, request: HttpRequest) -> HttpResponse:

        username:str = request.POST.get('name')
        password:str = request.POST.get('password')
        
        users = auth.authenticate(request,username=username,password=password)
        
        if users:
            auth.login(request, users)
            return redirect_url('listar')
        messages.add_message(request,constants.ERROR,'Username ou senha inválidos')
        return redirect_url('login')
class LogoutView(View):
    
    def get(self, request: HttpRequest) -> HttpResponse:
        auth.logout(request)
        return redirect_url('login')



