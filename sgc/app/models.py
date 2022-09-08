from django.db import models

# Create your models here.

class Curso (models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=50)
    estado=models.CharField(max_length=20)

class Usuario (models.Model):
    id=models.IntegerField(primary_key=True)
    tipoIdentificado=models.CharField(max_length=20)
    tUsuario=models.CharField(max_length=20)
    clave=models.CharField (max_length=20)
    nombre=models.CharField(max_length=20)
    apellidos=models.CharField(max_length=20)
    telefono=models.CharField(max_length=20)
    correo=models.CharField(max_length=20)
    genero=models.CharField(max_length=20)
    estado=models.BooleanField

class Materia (models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=20)

class Tarea (models.Model):
    id=models.IntegerField(primary_key=True)
    calificacion=models.IntegerField
    estado=models.CharField(max_length=20)
    nombre=models.CharField(max_length=20)
