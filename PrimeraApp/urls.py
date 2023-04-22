
from django.urls import path
from .views import *


urlpatterns = [
   
    path('', InicioApp),
    path('crear_curso/', crear_curso),
    path('Cursos/' , Cursos),
    path('Profesores/' , Profesores),
    path('Estudiantes/' , Estudiantes),
    path('Entregables/', Entregables ),

]
    