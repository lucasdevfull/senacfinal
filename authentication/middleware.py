from django.http import HttpRequest,Http404,HttpResponse
from backend.shortcuts import redirect_url
from django.urls import reverse_lazy
from typing import Callable
def admin_middleware(get_response: Callable[[HttpRequest], HttpResponse]) -> Callable[[HttpRequest], HttpResponse]:
    def middleware(request: HttpRequest):
        print(request.user)
        if request.user.is_authenticated and request.path == reverse_lazy('login'):
            if request.user.is_staff or request.user.is_superuser:
                return redirect_url('listar')
            else:
                return redirect_url('listar')
        
        response = get_response(request)
        return response
    
    return middleware
