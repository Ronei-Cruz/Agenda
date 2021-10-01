from django.http import response
from django.shortcuts import render
from core.models import Evento

# Create your views here.
""" def index(request):                     # redireciona url vazia direto para a url /agenda/
    return redirect('/agenda/') """

def listaEventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': evento}
    return render(request,'agenda.html', dados)