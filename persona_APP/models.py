from django.db import models
from persona_APP.choices import lista
from django.db import models

# Create your models here.

class Proyecto(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    fechainscripcion = models.DateField()
    institucion = models.CharField(max_length=50)
    horainscripcion = models.TimeField()
    estado = models.CharField(max_length=50, choices = lista)
    observacion = models.CharField(max_length=100, blank=True)

