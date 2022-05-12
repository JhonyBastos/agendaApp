from django.db import models
from django.contrib.auth.models import User
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