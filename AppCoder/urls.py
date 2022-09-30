from django.urls import path
from AppCoder import *
from AppCoder.views import buscar, busquedaProfes, entregables, estudiantes, formulario1, formulario2, inicio, profesores

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("estudiantes/", estudiantes, name="Estudiantes"),
    path("profesores/", profesores, name="Profesores"),
    path("entregables/", entregables, name="Entregables"),
    path("formulario/", formulario1, name="Formularios"),
    path("formulario2/", formulario2),
    path("busquedaProfes/", busquedaProfes, name="BusquedaProfes"),
    path("buscar/", buscar)
    
    ]