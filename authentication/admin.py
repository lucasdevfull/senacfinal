from django.contrib.auth import admin as admin_auth
from django.contrib import admin
from .models import User
from .forms import UserChangeForm,UserCreationForm

# Register your models here.
@admin.register(User)
class UserAdmin(admin_auth.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    fieldsets = admin_auth.UserAdmin.fieldsets + (
        ('Informações adicionais', 
         {'fields': (
             'data_nascimento',
                     'genero',
                     'telefone',
                     'pais',
                     'cidade',
                     'endereco',
                     'cep'
                     )
            }
        ),
    )
    