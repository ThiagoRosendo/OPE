from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404, HttpResponse
from django.contrib import messages
from .forms import *
from django.forms import modelformset_factory
from .models import *
from django.views.generic import TemplateView, ListView, DetailView
from django.forms import formset_factory, inlineformset_factory
from datetime import date


def check_data(data):
    hoje = date.today()
    if data < hoje:
        return False

def check_agenda(agenda, data, hora_inicio, hora_fim):

    inicio = []
    fim = []
    for item in agenda:
        if item.data == data:
            inicio.append(item.hora_inicio)
            fim.append(item.hora_fim)
    inicio.sort()
    fim.sort()
    if len(inicio) > 0:
        if hora_inicio > fim[-1]:
            return True

        for i in range(0, len(inicio)):
            cont = 1
            if (cont == len(inicio)):
                cont -= 1
            if hora_inicio == inicio[i]:
                return False
            elif hora_inicio < inicio[i] and hora_fim > inicio[i]: 
                return False
            elif hora_inicio > inicio[i] and hora_inicio < fim[i]: 
                return False
            elif hora_fim > inicio[cont]:
                return False
            elif hora_inicio >= hora_fim:
                return False
            cont += 1

    return True
        
    

def index(request):
    return render(request, 'index.html')


def cliente_cad(request):
    page = 'clientes/cliente_cad.html'
    
    if request.POST:
        form = ClienteCadForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect('web:cliente_detail', form.cpf)
    else:
        form = ClienteCadForm
    return render(request, page, {'form': form})


def cliente_edit(request, cpf):
    page = 'clientes/cliente_edit.html'
    cliente = ClienteModel.objects.get(cpf=cpf)
    form = ClienteCadForm(request.POST or None, instance=cliente)
    if request.POST:
        if form.is_valid() and 'salvar' in request.POST:
            form.save()
            return redirect('web:cliente_detail', cliente.cpf)
        if 'excluir' in request.POST:
            cliente.photo.delete()
            cliente.delete()
            return redirect('web:cliente_list')

    return render(request, page, {'form': form, 'cliente': cliente})


def cliente_list(request):
    page = 'clientes/cliente_list.html'
    clientes = ClienteModel.objects.all()
    clientes = clientes.order_by('nome')

    return render(request, page, {'clientes': clientes})


def cliente_detail(request, cpf):
    page = 'clientes/cliente_detail.html'
    cliente = ClienteModel.objects.filter(cpf=cpf)
    pedidos = Pedido.objects.filter(cliente=cpf)
    fichas = FichaAnamnese.objects.filter(cliente=cpf)

    return render(request, page, {'cliente': cliente, 'pedidos': pedidos, 'fichas': fichas})


def services_cad(request):
    page = 'services/services_cad.html'
    
    if request.POST:
        form = ServicesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Serviço cadastrado com sucesso!')
            return redirect('web:services_list')
    else:
        form = ServicesForm
    return render(request, page, {'form': form})


def services_edit(request, id):
    page = 'services/services_edit.html'
    services = Servicos.objects.get(id=id)
    form = ServicesForm(request.POST or None, instance=services)
    if request.POST:
        if form.is_valid() and 'salvar' in request.POST:
            form.save()
            return redirect('web:services_list')
        if 'excluir' in request.POST:
            services.delete()
            return redirect('web:services_list')

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


def novo_pedido(request):
    order_forms = Pedido()
    objetos = Servicos.objects.all()
    objetos = objetos.order_by('id')
    item_order_formset = inlineformset_factory(Pedido, PedidoDetail, form=PedidoDetailForm, extra=2,
                                               can_delete=False, min_num=1, validate_min=True
                                             )

    if request.method == 'POST':
        forms = PedidoForm(request.POST, request.FILES, instance=order_forms)
        formset = item_order_formset(request.POST, request.FILES, instance=order_forms, prefix='pedido_det')

        if forms.is_valid() and formset.is_valid():
            forms = forms.save(commit=False)
            forms.save()
            formset.save()
            return redirect('web:pedido_detail', forms.id)

    else:
        forms = PedidoForm(instance=order_forms)
        formset = item_order_formset(instance=order_forms, prefix='pedido_det')

    context = {
        'forms': forms,
        'formset': formset,
        'objetos': objetos,
    }

    return render(request, 'pedidos/novo_pedido.html', context)


def pedido_detail(request, id):
    page = 'pedidos/pedido_detail.html'
    pedido = Pedido.objects.filter(id=id)
    pedido_detail = PedidoDetail.objects.filter(pedido=id)
    agenda = Agenda.objects.filter(pedido=id)

    return render(request, page, {'pedido': pedido, 'pedido_detail': pedido_detail, 'agenda': agenda})


def ficha_anamnese(request, cpf):
    page = 'clientes/ficha_anamnese.html'
    cliente = ClienteModel.objects.filter(cpf=cpf)
    if request.POST:
        form = AnamneseForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            messages.success(request, 'Ficha cadastrada com sucesso!')
            return redirect('web:ficha_anamnese_p', form.cliente.cpf)
    else:
        form = AnamneseForm
    return render(request, page, {'form': form, 'cliente': cliente})

def ficha_anamnese_p(request, cpf):
    page = 'clientes/ficha_anamnese_p.html'
    ficha = FichaAnamnese.objects.filter(cliente=cpf)

    return render(request, page, {'ficha': ficha})


def agendar_sessao(request, id, sessao):
    page = 'pedidos/agendar_sessao.html'
    pedido_detail = PedidoDetail.objects.filter(pedido=id)
    pedido = Pedido.objects.filter(id=id)
    agenda = Agenda.objects.all()
    n_sessao = sessao
    if request.POST:
        form = AgendaForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            if check_data(form.data) is False:
                messages.error(request, 'Não é possível agendar um atendimento para uma data anterior a hoje!')
                form = AgendaForm
            elif check_agenda(agenda, form.data, form.hora_inicio, form.hora_fim) is False:
                messages.error(request, 'Horário não disponível')
                form = AgendaForm
            else:
                form.save()
                return HttpResponse('<script>window.close(); window.opener.location.reload();</script>')
        else:
            raise Exception('Erro')
            
    else:
        form = AgendaForm
    return render(request, page, {'form': form, 'pedido': pedido, 'pedido_detail': pedido_detail, 'agenda': agenda, 'n_sessao': n_sessao})

