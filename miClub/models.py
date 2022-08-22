from django.db import models

# Create your models here.
class Directivos(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    n_socio = models.IntegerField()
    cargo = models.CharField(max_length=20)

class Socios(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    n_socio = models.IntegerField()
    fecha_ingreso = models.DateField()
    email = models.EmailField()

class Diciplina(models.Model):

    deporte = models.CharField(max_length=30)
    lugar = models.CharField(max_length=30)

class Cuota(models.Model):

    n_socio = models.IntegerField()
    fecha_cuota = models.DateField()
    deporte = models.CharField(max_length=30)
    pago = models.BooleanField()