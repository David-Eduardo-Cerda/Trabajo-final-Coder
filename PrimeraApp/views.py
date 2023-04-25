from django.shortcuts import render 
from .models import Curso , Profesor
from django.http import HttpResponse



"""def crear_curso(request):
      

      nombre_curso = "Python"
      comision_curso = 51325

      curso = Curso(nombre = nombre_curso, comision = comision_curso)

      curso.save()

      respuesta = f"Curso creado --- {nombre_curso} --- {comision_curso}"

      return HttpResponse(respuesta)"""


def Cursos(request):
      return render(request , 'template/Cursos.html') 
 
def Estudiantes(request):
      return render (request ,'template/Estudiantes.html') 

def Profesores(request):
      profesores = Profesor.objects.all()
      context = {"profesores": profesores}
      return render (request,'template/Profesores.html', context) 

def Entregables(request):
      return render (request, 'template/Entregables.html') 

def inicio(request):
      return render(request ,'template/inicio.html')

def InicioApp(request):
      return render(request ,'template/InicioApp.html')
