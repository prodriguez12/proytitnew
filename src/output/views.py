# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from output.models import Output

# Create your views here.
@login_required(login_url='/users/login/')
def output_single_view(request, output_id):
	#return  HttpResponse("<h1>Entrega Sprint 2</h1>")
	obj = Output.objects.get(id=output_id)
	context = {
		"titulo": "Output " + str(obj.id),
		"output": obj,

	}
	return render(request, "Output/view.html", context)

@login_required(login_url='/users/login/')
def output_list_view(request, *args, **kwargs):
	#return  HttpResponse("<h1>Entrega Sprint 2</h1>")
	lista = Output.objects.filter(origin__owner__pk=request.user.id)
	print(lista)
	context = {
		"titulo": "Listado de Outputs",
		"lista": lista
	}
	return render(request, "Output/list.html", context)

@login_required(login_url='/users/login/')
def input_output_list_view(request, *args, **kwargs):
	#return  HttpResponse("<h1>Entrega Sprint 2</h1>")
	lista = Output.objects.all()
	print(lista)
	context = {
		"titulo": "Listado de Outputs",
		"lista": lista
	}
	return render(request, "Output/list.html", context)