# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from zipfile import *
from .form import InputForm
from .models import Input

# Create your views here.
@login_required(login_url='/users/login/')
def input_new_view(request, *args, **kwargs):
	#return  HttpResponse("<h1>Entrega Sprint 2</h1>")
	form = InputForm(request.POST or None, request.FILES)
	if form.is_valid():
		if request.user.is_authenticated():
			instance = form.save(commit=False)
			instance.owner = request.user
			form.save()
			return redirect('/inputs/')
		else:
			return render(request,'home.html',context)
	if form.errors:
		errors = form.errors
	context = {
		"titulo": "nuevo input",
		"formulario": form
	}
	return render(request, "input/new.html", context)

@login_required(login_url='/users/login/')
def input_single_view(request, input_id):
	#return  HttpResponse("<h1>Entrega Sprint 2</h1>")
	obj = Input.objects.get(id=input_id)
	context = {
		"titulo": "Input " + str(obj.id),
		"input": obj,

	}
	return render(request, "input/view.html", context)

@login_required(login_url='/users/login/')
def input_list_view(request, *args, **kwargs):
	#return  HttpResponse("<h1>Entrega Sprint 2</h1>")
	lista = Input.objects.all()
	print(lista)
	context = {
		"titulo": "Listado de inputs",
		"lista": lista
	}
	return render(request, "input/list.html", context)