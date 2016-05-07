

from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Cliente (models.Model):
	nome = models.CharField(verbose_name = 'Nome', max_length = 100)
	saldo = models.DecimalField(verbose_name = 'Saldo', max_digits = 15, decimal_places, default=0)
	foto = models.ImageField(upload_to = 'cliente/', height_field = None, width_field = None, max_length = 100, blanck = True, default = 'Cliente/no_foto.jpg')
	cliente = models.Manager()

	def  __str__(self):
		return self.nome
class LancamentoCliente(models.Model):
	CD = (
		('Crédito', (
			('CD', 'Creditar'),
			('CE', 'Estonar Crédito'),
			)
		),
		('Débito', (
			('DD', 'Debitar'),
			('ED', 'Estonar Débito'),
			)
		),
	)

	cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
	cd = models.CharField(max_length = 2, choices = CD, verbose_name= 'Tipo de Lançamento')
	saldoanterior = models.DecimalField(verbose_name = 'Saldo Anterior', max_digits = 15, decimal_places = 2, default = 0)
	valor = models.DecimalField(verbose_name = 'Valor', max_digits = 15, decimal_places = 2, default = 0)
	data = models.DataTimeField(verbose_name = 'Data', auto_now = False, auto_now_add = True)
	lancamentocliente = models.Manager()

	def __unicode__(self):
		return self.cliente.nome
