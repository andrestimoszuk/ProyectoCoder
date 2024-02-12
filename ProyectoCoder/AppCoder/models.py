from django.db import models
    
class Paciente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
   
class Medico(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
   
class Visita(models.Model):
    fecha = models.DateField()
    sede = models.CharField(max_length=30)