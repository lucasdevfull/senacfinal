from django.contrib import admin
from .models import Pessoa,Cargo,Pedido

# Register your models here.
class PedidoInline(admin.TabularInline):
    readonly_fields = ('nome','quantidade','descricao',)
    list_display = ('nome','email','descricao')
    model = Pedido
    extra = 0
@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    inlines = [PedidoInline]
    list_display = ('nome','email','cargo','nome_completo',) #o q aparece
    readonly_fields = ('senha','cargo',) #leitura
    search_fields = ('nome',) #pesquisa
    list_filter = ('cargo',) #filtro
    #list_editable = ('nome',) edito sem entrar em outra página

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_filter = ('cargo',)


