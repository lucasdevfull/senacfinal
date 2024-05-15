from django.shortcuts import render,redirect
from .models import User
from django.http import HttpResponse,HttpRequest
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

    try:
        user=User.objects.create_user(username=username,email=email,password=password)
        return HttpResponse(user)
    except:
        return HttpResponse('não foi') 

def login(request:HttpRequest) -> HttpResponse:
    template_name = "registration/login.html"
    return render(request,template_name)