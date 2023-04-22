from django.db import models


class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellitod = models.CharField(max_length=30)
    email = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellitod = models.CharField(max_length=30)
    email = models.EmailField()
    profecion = models.CharField(max_length=30)

class Entregables(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField(max_length=20)
    entregado = models.BooleanField()
    