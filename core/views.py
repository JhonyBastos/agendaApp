from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime, timedelta
from django.http.response import Http404, JsonResponse

# Create your views here.

# Redireciona o index para a view
# def index(request):
#     return redirect('/agendaApp/')

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request): #validação do usuário e login
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou Senha inválidos. Digite novamente.")

    return redirect('/')

@login_required(login_url='/login/') #envia a sessão não logada para a page de login
def lista_eventos(request):     #lista os eventos
    usuario = request.user
    data_atual = datetime.now() - timedelta(hours=1)
    # utilizar .get(opção desejada) para pegar um valor especifico ou .all para todos
    evento = Evento.objects.filter(usuario=usuario,
                                   data_evento__gt=data_atual) # __gt para pegar valor maior e __lt para valor menor
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)

@login_required(login_url='/login/')
def evento(request):    #view de criação de evento e de alteração
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
    return render(request, 'evento.html', dados)

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        id_evento = request.POST.get('id_evento')
        if id_evento:
            evento = Evento.objects.get(id=id_evento)
            if evento.usuario == usuario:   #valida se é o usuário criador que está fazendo atualização
                evento.titulo = titulo
                evento.data_evento = data_evento
                evento.descricao = descricao
                evento.save()
            #Evento.objects.filter(id=id_evento).update(titulo=titulo,
            #                                           data_evento=data_evento,
            #                                           descricao=descricao)
        else:
            Evento.objects.create(titulo=titulo,
                                  data_evento=data_evento,
                                  descricao=descricao,
                                  usuario=usuario)
    return redirect('/')

@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    try:
        evento = Evento.objects.get(id=id_evento)
    except Exception:
        raise Http404()  #tratamento de erros
    if usuario == evento.usuario:
        evento.delete()
    else:
        raise Http404()
    return redirect('/')


def json_lista_evento(request, id_usuario):
    usuario = User.objects.get(id=id_usuario)   #para requisição externa, sem necessidade de login
    evento = Evento.objects.filter(usuario=usuario).values('id', 'titulo')
    return JsonResponse(list(evento), safe=False)  #Converter a lista para um Json