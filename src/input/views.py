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
	gbd_path = obj.gbd.path
	gbdzip = zipfile.ZipFile(gbd_path)
	folder_path = gbd_path.split(".")[0]
	if(not os.path.isdir(folder_path)):
		gbdzip = zipfile.ZipFile(obj.gbd.path)
		gbdzip.extractall()
		gbdzip.close()
		obj.gbd_root = folder_path
		obj.save()
	else:
		os.remove(obj.gbd.path)
		filePaths = retrieve_file_paths(folder_path)
		gbdzip = zipfile.ZipFile(obj.gbd.path,'w')
		with gbdzip:
			for file in filePaths:
				gbdzip.write(file)
	if(obj.owner.id == request.user.id):
		context = {
			"titulo": "Input " + str(obj.id),
			"input": obj,

		}
		return render(request, "input/view.html", context)
	else:
		return render('home')

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

# funcion para ayudar con la actualizacion de los archivos zip de las geo base de datos
# obtenido desde https://linuxhint.com/python_zip_file_directory/
def retrieve_file_paths(dirName):
 
  # setup file paths variable
  filePaths = []
   
  # Read all directory, subdirectories and file lists
  for root, directories, files in os.walk(dirName):
    for filename in files:
        # Create the full filepath by using os module.
        filePath = os.path.join(root, filename)
        filePaths.append(filePath)
         
  # return all paths
  return filePaths