from typing import Any
from django.contrib.auth.backends import ModelBackend, UserModel
from django.db.models import Q 
from django.http.request import HttpRequest
from .models import User

class MyBackend(ModelBackend):
    def authenticate(self,request: HttpRequest,username: str = None,password: str = None,**kwargs: Any,) -> User | None:
        try:

            user = User.objects.filter(Q (email__iexact=username) | Q(username__iexact=username))

        except UserModel.DoesNotExist:
            return None
    
        if user.exists():
            user=user.first()
            if user.check_password(password):
                return user
        
        