from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ClienteCadForm, ServicesForm
from .models import ClienteModel, Servicos


def index(request):
    return render(request, 'index.html')


def cliente_cad(request):
    page = 'clientes/cliente_cad.html'
    
    if request.POST:
        form = ClienteCadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect('cliente_list')
    else:
        form = ClienteCadForm
        messages.warning(request, 'Ops! Verifique os dados digitados!')
    return render(request, page, {'form': form})


def cliente_edit(request, cpf):
    page = 'clientes/cliente_edit.html'
    cliente = ClienteModel.objects.get(cpf=cpf)
    form = ClienteCadForm(request.POST or None, request.FILES, instance=cliente)
    if request.POST:
        if form.is_valid() and 'salvar' in request.POST:
            form.save()
            return redirect('cliente_list')
        if 'excluir' in request.POST:
            cliente.delete()
            return redirect('cliente_list')

    return render(request, page, {'form': form, 'cliente': cliente})


def cliente_list(request):
    page = 'clientes/cliente_list.html'
    clientes = ClienteModel.objects.all()
    clientes = clientes.order_by('nome')

    return render(request, page, {'clientes': clientes})


def cliente_detail(request, cpf):
    page = 'clientes/cliente_detail.html'
    cliente = ClienteModel.objects.filter(cpf=cpf)

    return render(request, page, {'cliente': cliente})


def services_cad(request):
    page = 'services/services_cad.html'
    form = ServicesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('services_list')

    return render(request, page, {'form': form})


def services_edit(request, id):
    page = 'services/services_edit.html'
    services = Servicos.objects.get(id=id)
    form = ServicesForm(request.POST or None, instance=services)
    if request.POST:
        if form.is_valid() and 'salvar' in request.POST:
            form.save()
            return redirect('services_list')
        if 'excluir' in request.POST:
            services.delete()
            return redirect('services_list')

    return render(request, page, {'form': form, 'services': services})


def services_list(request):
    page = 'services/services_list.html'
    services = Servicos.objects.all()
    services = services.order_by('nome')

    return render(request, page, {'services': services})


def services_detail(request, id):
    page = 'services/services_detail.html'
    services = Servicos.objects.filter(id=id)

    return render(request, page, {'services': services})