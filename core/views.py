from django.shortcuts import render, redirect
from core.models import Evento
# Create your views here.

# Redireciona o index para a view
# def index(request):
#     return redirect('/agendaApp/')

def lista_eventos(request):
    usuario = request.user

    # utilizar .get(opção desejada) para pegar um valor especifico ou  filtrar com .filter(usuario=usuario)
    evento = Evento.objects.all
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)
