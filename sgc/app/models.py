from django.db import models

# Create your models here.

class Proyecto (models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=50, unique=True)
    estado=models.CharField(max_length=20)

class Usuario (models.Model):
    id=models.IntegerField(primary_key=True)
    tipoIdentificado=models.CharField(max_length=20)
    tUsuario=models.CharField(max_length=20)
    clave=models.CharField (max_length=20)
    nombre=models.CharField(max_length=20)
    apellidos=models.CharField(max_length=20)
    telefono=models.CharField(max_length=20)
    correo=models.CharField(max_length=20, unique=True)
    genero=models.CharField(max_length=20)
    estado=models.BooleanField
    idProyecto=models.ForeignKey(Proyecto, on_delete=models.RESTRICT, null=True, blank=True)
    notaDefinitivaProyecto=models.DecimalField(max_digits=3, decimal_places=2, null=True)

