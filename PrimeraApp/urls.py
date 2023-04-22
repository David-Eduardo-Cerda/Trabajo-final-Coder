
from django.urls import path
from PrimeraApp import views 
from PrimeraApp import Template


urlpatterns = [
   
    path('', views.InicioApp),
    path('crear_curso/', views.crear_curso , name="Cursos"),
    path('Cursos/' , views.Cursos),
    path('Profesores/' , views.Profesores),
    path('Estudiantes/' , views.Estudiantes),
    path('Entregables/', views.Entregables ),

]
    