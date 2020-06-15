from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from django.forms import modelformset_factory
from .models import *
from django.views.generic import TemplateView, ListView, DetailView
from django.forms import formset_factory, inlineformset_factory
from datetime import date, timedelta


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
        if hora_inicio >= fim[-1]:
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
        
    
def login_view(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('web:index')
            
        else:
            messages.error(request, 'Usuário ou senha inválidos!')
            return redirect('web:login')
            # Return an 'invalid login' error message.

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('web:login')


@login_required
def index(request):
    pedidos = Pedido.objects.filter(data__year=date.today().year)
    despesas = Despesas.objects.filter(vencimento__year=date.today().year).order_by('vencimento')
    registros = RegistroSessao.objects.all()
    data = date.today()
    semana = []
    for i in range(0 - data.weekday(), 7 - data.weekday()):
        semana.append(data + timedelta(days=i))   
    agenda = Agenda.objects.filter(data=data).order_by('hora_inicio')
    agenda_semanal = Agenda.objects.filter(data__range=[semana[0], semana[-1]]).order_by('data', 'hora_inicio')
    if request.POST:
        if 'registrar' in request.POST:
            form = RegistroSessaoForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                try:
                    registro = RegistroSessao.objects.get(agendamento=form.agendamento.id)
                    form = RegistroSessaoForm(request.POST, instance=registro)
                    form = form.save(commit=False)
                    messages.success(request, 'O registro da sessão %s de %s foi atualizado.' % (form.agendamento.sessao, form.agendamento.servico))
                    form.save()
                except:
                    messages.success(request, 'O registro da sessão %s de %s foi realizado com sucesso!' % (form.agendamento.sessao, form.agendamento.servico))
                    form.save()
                return redirect('web:index')
            else:
                raise Exception('erro')
        
        if 'despesa' in request.POST:
            form = DespesasForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.save()
                messages.success(request, '"%s" foi registrado no relatório de despesas.' % form.descricao)
                return redirect('web:index')
            else:
                raise Exception('erro')

    context = {'agenda': agenda, 'agenda_semanal': agenda_semanal,
               'pedidos': pedidos, 'registros': registros, 'despesas': despesas
                }

    return render(request, 'index.html', context)

@login_required
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


@login_required
def cliente_edit(request, cpf):
    page = 'clientes/cliente_edit.html'
    cliente = ClienteModel.objects.get(cpf=cpf)
    form = ClienteCadForm(request.POST or None, instance=cliente)
    if request.POST:
        if form.is_valid() and 'salvar' in request.POST:
            form.save()
            return redirect('web:cliente_detail', cliente.cpf)
        if 'excluir' in request.POST:
            if 'default.jpg' != cliente.photo:
                cliente.photo.delete()
            cliente.delete()
            return redirect('web:cliente_list')

    return render(request, page, {'form': form, 'cliente': cliente})

@login_required
def cliente_del(request, cpf):
    page = 'clientes/del_cliente.html'
    cliente = ClienteModel.objects.get(cpf=cpf)
    form = ClienteCadForm(request.POST)
    if request.POST:
        if 'default.jpg' != cliente.photo:
            cliente.photo.detele()
        cliente.delete()
        messages.warning(request, 'O cadastro de %s foi exlcuído com sucesso!' % cliente.nome)
        return redirect('web:cliente_list')

    return render (request, page, {'cliente': cliente, 'form': form})

@login_required
def cliente_list(request):
    page = 'clientes/cliente_list.html'
    clientes = ClienteModel.objects.all()
    clientes = clientes.order_by('nome')

    return render(request, page, {'clientes': clientes})


@login_required
def cliente_detail(request, cpf):
    page = 'clientes/cliente_detail.html'
    cliente = ClienteModel.objects.get(cpf=cpf)
    pedidos = Pedido.objects.filter(cliente=cpf)
    fichas = FichaAnamnese.objects.filter(cliente=cpf)
    ultimo_pedido = pedidos.last() if len(pedidos) > 0 else ''
    pedido_detail = {}
    pd = []
    for pedido in pedidos:
        objetos = PedidoDetail.objects.filter(pedido=pedido.id)
        pedido_detail[pedido.id] = []
        for item in objetos:
            pedido_detail[pedido.id].append(item.servico)
    for item in pedido_detail:
        if len(pedido_detail[item]) == 2:
            pd.append(pedido_detail[item][0] + ' e mais 1 serviço')
        elif len(pedido_detail[item]) > 1:
                pd.append(pedido_detail[item][0] + ' e mais %d serviços' % (len(pedido_detail[pedido.id]) - 1))
        else:
                pd.append(pedido_detail[item][0])

    return render(request, page, {'cliente': cliente, 'pedidos': pedidos, 'fichas': fichas, 'ultimo_pedido': ultimo_pedido, 'pd': pd})


@login_required
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


@login_required
def services_edit(request, id):
    page = 'services/services_edit.html'
    services = Servicos.objects.get(id=id)
    form = ServicesForm(request.POST or None, instance=services)
    if request.POST:
        if form.is_valid() and 'salvar' in request.POST:
            form.save()
            messages.success(request, 'O serviço de %s foi atulizado com sucesso!' % services.nome)
            return redirect('web:services_list')
        if 'excluir' in request.POST:
            messages.warning(request, 'O serviço de %s foi excluído!' % services.nome)
            services.delete()
            return redirect('web:services_list')

    return render(request, page, {'form': form, 'services': services})


@login_required
def services_list(request):
    page = 'services/services_list.html'
    services = Servicos.objects.all()
    services = services.order_by('nome')

    return render(request, page, {'services': services})


@login_required
def services_detail(request, id):
    page = 'services/services_detail.html'
    services = Servicos.objects.filter(id=id)

    return render(request, page, {'services': services})


@login_required
def novo_pedido(request):
    order_forms = Pedido()
    clientes = ClienteModel.objects.all()
    clientes = clientes.order_by('nome')
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
            messages.success(request, 'Pedido registrado com sucesso!')
            return redirect('web:pedido_detail', forms.id)

    else:
        forms = PedidoForm(instance=order_forms)
        formset = item_order_formset(instance=order_forms, prefix='pedido_det')

    context = {
        'forms': forms,
        'formset': formset,
        'objetos': objetos,
        'clientes': clientes
    }

    return render(request, 'pedidos/novo_pedido.html', context)


@login_required
def novo_pedido_cliente(request, cpf):
    cliente = ClienteModel.objects.get(cpf=cpf)
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
            messages.success(request, 'Pedido registrado com sucesso!')
            return redirect('web:pedido_detail', forms.id)

    else:
        forms = PedidoForm(instance=order_forms)
        formset = item_order_formset(instance=order_forms, prefix='pedido_det')

    context = {
        'forms': forms,
        'formset': formset,
        'objetos': objetos,
        'cliente': cliente
    }

    return render(request, 'pedidos/novo_pedido_cliente.html', context)


@login_required
def pedido_detail(request, id):
    page = 'pedidos/pedido_detail.html'
    pedido = Pedido.objects.get(id=id)
    pedido_detail = PedidoDetail.objects.filter(pedido=id)
    agenda_pedido = Agenda.objects.filter(pedido=id)
    agenda = Agenda.objects.all()
    registros = RegistroSessao.objects.all()
    if request.POST:
        if 'agendar' in request.POST:
            form = AgendaForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                try:
                    agendamento = Agenda.objects.get(id=form.id)
                    form = AgendaForm(request.POST, instance=agendamento)
                    form = form.save(commit=False)
                    messages.success(request, 'Sessão %s para o serviço de %s foi agendada atualizada!' % (form.sessao, form.servico))
                    form.save()
                except:
                    if check_data(form.data) is False:
                        messages.error(request, 'Não é possível agendar um atendimento para uma data anterior a hoje!')
                        form = AgendaForm
                    elif check_agenda(agenda, form.data, form.hora_inicio, form.hora_fim) is False:
                        messages.error(request, 'Horário não disponível')
                        form = AgendaForm
                    else:
                        messages.success(request, 'Sessão %s para o serviço de %s foi agendada com sucesso!' % (form.sessao, form.servico))
                        form.save()
                return redirect('web:pedido_detail', form.pedido.id)
        if 'registrar' in request.POST:
            form = RegistroSessaoForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                try:
                    registro = RegistroSessao.objects.get(agendamento=form.agendamento.id)
                    form = RegistroSessaoForm(request.POST, instance=registro)
                    form = form.save(commit=False)
                    messages.success(request, 'O registro da sessão %s de %s foi atualizado.' % (form.agendamento.sessao, form.agendamento.servico))
                    form.save()
                except:
                    messages.success(request, 'O registro da sessão %s de %s foi realizado com sucesso!' % (form.agendamento.sessao, form.agendamento.servico))
                    form.save()
                return redirect('web:pedido_detail', pedido.id)
            else:
                raise Exception('erro')
            
    else:
        form = AgendaForm

    context = {
        'pedido': pedido, 'pedido_detail': pedido_detail,
        'agenda': agenda, 'agenda_pedido': agenda_pedido, 'form': form,
        'registros': registros
        }

    return render(request, page, context )


@login_required
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

@login_required
def ficha_anamnese_p(request, cpf):
    page = 'clientes/ficha_anamnese_p.html'
    ficha = FichaAnamnese.objects.filter(cliente=cpf)

    return render(request, page, {'ficha': ficha})

@login_required
def del_agendamento(request, id):
    page = 'pedidos/del_agendamento.html'
    agendamento = Agenda.objects.get(id=id)
    form = AgendaForm(request.POST)
    if request.POST:
        agendamento.delete()
        messages.warning(request, 'Sessão %s do serviço de %s foi cancelada!' % (agendamento.sessao, agendamento.servico))
        return redirect('web:pedido_detail', agendamento.get_pedido())

    return render(request, page, {'form': form, 'agendamento': agendamento})

@login_required
def confirmar_pgto(request, id):
    page = 'despesas/confirmar_pgto.html'
    despesa = Despesas.objects.get(id=id)
    if request.POST:
        despesa.status = '1'
        despesa.save()
        messages.success(request, 'O pagamento "%s" foi confirmado.' % despesa.descricao)
        return redirect('web:index')
    return render(request, page, {'despesa': despesa})

def busca(request):
    query = request.GET.get('search', '')
    if query:
        clientes = ClienteModel.objects.filter(nome__icontains=query).order_by('nome')
        pedidos_detail = PedidoDetail.objects.filter(servico__icontains=query)

    context = {'clientes': clientes, 'pedidos_detail': pedidos_detail,
                'query': query
                }

    return render(request, 'busca.html', context)


