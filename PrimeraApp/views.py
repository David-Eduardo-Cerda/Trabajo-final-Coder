from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse


def crear_curso(request):
      

      nombre_curso = "Python"
      comision_curso = "david"

      curso = Curso(nombre = nombre_curso, comision = comision_curso)

      curso.save()

      respuesta = f"Curso creado --- {nombre_curso} --- {comision_curso}"

      return HttpResponse(respuesta)