from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data de Criação')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Criado por:') #pegando o usuário do djangoAdmin

    class Meta:
        db_table = 'evento'

    def __str__(self):  # define a forma como o registro vai se comportar
        return self.titulo

    def get_data_evento(self):          # altera o padrão de apresentação da data
        return self.data_evento.strftime('%d/%m/%Y %Hh%M min')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M') #padrão para a alteração da data

    def get_evento_atrasado(self):  #verifica se o evento está atrasado
        if self.data_evento < datetime.now():
            return True
        else:
            return False