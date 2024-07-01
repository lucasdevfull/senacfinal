from django.shortcuts import redirect
from django.urls import reverse_lazy
def redirect_url(url:str):
    return redirect(reverse_lazy(url))