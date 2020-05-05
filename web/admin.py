from django.contrib import admin
from .models import *

admin.site.register(ClienteModel),
admin.site.register(Servicos),
admin.site.register(PedidoDetail),
admin.site.register(Pedido),
admin.site.register(FichaAnamnese)
admin.site.register(Agenda)
# admin.site.register(Author)
# admin.site.register(Book)


# Register your models here.
