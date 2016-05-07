# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import aunthenticate, logout, login

from cadastro.models import *
from cadastro.forms import *

# Create your views here.

def index(request):
	try: 
		if request.session['usuario'] == '':
			request.session['usuario'] = ''
	except:
		request.session['usuario'] = ''
	return render (request, 'index.html',{
		'usuario': request.session['usuario']
		})

@login_required(login_url = '/entrar/')
def cliente(request):
	if request.method == 'POST':
		amsg = []
		form = FormLocalizaCliente(request.POST)
		if form.is_valid():
			cnome = form.cleaned_data.get('nome')
			cl = Cliente.cliente.filter(nome__contains=cnome)
		else:
			cl = Cliente.cliente.all()
	else:
		cl = Cliente.cliente.all()
		form = FormLocalizaCliente()
	return render(request, 'cliente.html',{
		'form': form,
		'cliente': cl
		})
@login_required(login_url = '/entrar/')
def lancamentocliente(request):
	if request.method == 'POST':
		amsg = []
		form = FormLocalizaCliente(request.POST)
		if form.isvalid():
			cnome = form.cleaned_data.get('nome')
			cl = LancamentoCliente.lancamentocliente.filter(cliente__nome__contains = cnome)
		else:
			cl = LancamentoCliente.lancamentocliente.all()
	else: 
		cl = LancamentoCliente.lancamentocliente.all()
		form = FormLocalizaCliente()

	return render (request, 'lancamentocliente.html', {
		'form': form
		'cliente': cl
		})
@login_required(login_url = '/entrar/')
def editarcliente(request, id_cliente):
	cmsg=''
	cl = Cliente.cliente.get(pk = id_cliente)
	if request.method == "POST":
		form = FormCliente(request.POST, request.FILES, instance = cl)
		if form.is_valid():
			print form
			from.save()
			cmsg = 'Dados salvos com sucesso.'
	else:
		form = FormCliente(instance = cl)
	return render(request, 'editarcliente.html'),
		{
		'cliente': cl,
		'msg': cmsg,
		'form': form
		})
@login_required(login_url = '/entrar/')
def excluircliente(request, id_cliente):
	cl = Cliente.cliente.get(pk = id_cliente)
	cmsg = ''
	nmsg1 = 0
	if cl.saldo > 0 :
		cmsg = 'Cliente não pode ser excluído, tem saldo.'
	else:
		nmsg1 = 1
		cmsg = 'Cliente excluído com sucesso.'
		cl.delete()
	return render(request, 'excluircliente.html',
		{
		'msg': cmsg,
		'nmsg': nmsg1
		})
@login_requires(login_url = '/entrar/')
def incluirlancamentocliente(request, id_cliente):
	cmsg = ''
	if resquet.method == "POST":
		form = FormLancamentoCliente(request.POST, request.FILES)
		if form.is_valid():
			ccd = form.cleaned_data.get('cd')
			nvalor = form.cleaned_data.get('valor')
			cl = Cliente.cliente.get(pk = id_cliente)
			nsaldo = cl.saldo
			la = LancamentoCliente.lancamentocliente.create(cliente_id = id_cliente, cd = ccd, valor = nvalor, saldoanterior = nsaldo)
			if ccd == 'CD':
				cl.saldo += nvalor
			elif ccd == 'CE':
				cl.saldo -= nvalor
			elif ccd == 'DD':
				cl.saldo -= nvalor
			elif ccd == 'DE':
				cl.saldo += nvalor
			cl.save()
			csmg = 'Dados salvos com sucesso.'
	else:
		form = FormLancamentoCliente()
	return render(request, 'incluirlancamentocliente.html',
		{
		'msg': cmsg,
		'form': form
		})
