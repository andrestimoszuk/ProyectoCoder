from django.contrib import admin
from AppCoder import models

# Register your models here. 
admin.site.register(models.Paciente)
admin.site.register(models.Medico)
admin.site.register(models.Visita)