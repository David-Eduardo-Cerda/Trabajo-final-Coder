from django.shortcuts import render 
from .models import Curso 
from django.http import HttpResponse



def crear_curso(request):
      

      nombre_curso = "Python"
      comision_curso = 51325

      curso = Curso(nombre = nombre_curso, comision = comision_curso)

      curso.save()

      respuesta = f"Curso creado --- {nombre_curso} --- {comision_curso}"

      return HttpResponse(respuesta)


def Cursos(request):
      return render(request , 'Template/Cursos.html') 
 
def Estudiantes(request):
      return render (request ,'Template/Estudiantes.html') 

def Profesores(request):
      return HttpResponse ('estos son los profesores') 

def Entregables(request):
      return HttpResponse ('estos son los entregables') 

def Inicio(request):
      return HttpResponse('Bienvenido a la paginaprincipal')

def InicioApp(request):
      return HttpResponse('Bienvenidos a la pagina principal de la app')
