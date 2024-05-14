from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
# Create your views here.
def register(request:HttpRequest) -> HttpResponse:
    template_name = "registration/cadastro.html"
    return render(request,template_name)

def login(request:HttpRequest) -> HttpResponse:
    template_name = "registration/login.html"
    return render(request,template_name)