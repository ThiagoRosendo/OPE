from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *

admin.site.register(ClienteModel),
admin.site.register(Servicos),
admin.site.register(PedidoDetail),
admin.site.register(Pedido),
admin.site.register(FichaAnamnese)
admin.site.register(Agenda)
admin.site.register(RegistroSessao)
admin.site.register(Despesas)

class UsuarioInline(admin.StackedInline):
    model = Usuario
    can_delete = False
    verbose_name_plural = 'usuários'

class UserAdmin(BaseUserAdmin):
    inlines = (UsuarioInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

