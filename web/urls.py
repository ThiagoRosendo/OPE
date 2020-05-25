"""gcd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import web.views as views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'web'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('', views.index, name='index'),
    path('clientes/cadastrar/', views.cliente_cad, name='cliente_cad'),
    path('clientes/lista/', views.cliente_list, name='cliente_list'),
    path('clientes/<cpf>', views.cliente_detail, name='cliente_detail'),
    path('clientes/<cpf>/edit', views.cliente_edit, name='cliente_edit'),
    path('clientes/<cpf>/del', views.cliente_del, name='cliente_del'),
    path('services/cadastrar', views.services_cad, name='services_cad'),
    path('services/lista', views.services_list, name='services_list'),
    path('services/<id>', views.services_detail, name='services_detail'),
    path('services/<id>/edit', views.services_edit, name='services_edit'),
    path('pedidos/novo_pedido/', views.novo_pedido, name='novo_pedido'),
    path('pedidos/novo_pedido/<cpf>', views.novo_pedido_cliente, name='novo_pedido_cliente'),
    path('pedido/<id>', views.pedido_detail, name='pedido_detail'),
    path('clientes/<cpf>/ficha', views.ficha_anamnese, name='ficha_anamnese'),
    path('clientes/<cpf>/print-ficha', views.ficha_anamnese_p, name='ficha_anamnese_p'),
    path('pedido/agenda/<id>/del', views.del_agendamento, name='del_agendamento'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
