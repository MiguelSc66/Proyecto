from distutils.log import INFO
from django.shortcuts import render
from calendar import c
from django.http import HttpResponse
from django.template import Template,  Context
"""""
from AppCoder.models import *
from AppCoder.forms import *
"""


def inicio(request): 

	return render(request, "ProyectoCoder/inicio.html")

def estudiantes(request):
	
	return render(request, "ProyectoCoder/estudiantes.html")

def profesores(request): 
	
	return render(request, "ProyectoCoder/profesores.html")

def entregables(request):
	
	ente1 = entregable(nombre="examen 1", fechaDeEntrega="2022-03-30")
	ente1.save()
	
	return render(request, "ProyectoCoder/entregables.html")


def curso1(request):
	return render(request, "ProyectoCoder/curso.html")

