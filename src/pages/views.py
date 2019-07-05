# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from output.models import Output
from input.models import Input
from datetime import datetime
import zipfile

# Create your views here.
def home_view(request, *args, **kwargs):
	#return  HttpResponse("<h1>Entrega Sprint 2</h1>")
	context = {
		"titulo": "Homepage"
	}
	return render(request, "home.html", context)

@login_required(login_url='/users/login/')
def apply_view(request, input_id):
	if request.method == 'POST':
		user = request.user
		inpt = Input.objects.get(id=input_id)
		root = inpt.gbd_root
		spd_tol = int(request.POST['spd_tol'])
		buffr = int(request.POST['buffr'])
		n_freq = int(request.POST['n_freq'])
		np = int(request.POST['np'])
		input_data = inpt.GPS_layer
		start = datetime.now()
		final_layer = algoritmo(root,spd_tol,buffr,n_freq,np,input_data)
		finish = datetime.now()
		new_output = Output(origin = inpt, owner = user, start = start, finish = finish, clean_layer = final_layer, 
			spd_tol = spd_tol,buffr = buffr, n_freq = n_freq, n_points = np)
		new_output.save()
		lista = inpt.output_set.all()
		context = {
			"titulo": "Listado de Outputs",
			"lista": lista
		}

		return render(request, "Output/list.html", context)