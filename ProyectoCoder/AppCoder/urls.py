from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('paciente', views.paciente, name="Paciente"),
    path('medico', views.medico, name="Medico"),
    path('visita', views.visita, name="Visita"),
    path('busqueda', views.busqueda, name="Busqueda"),
    path('resultado', views.resultado, name="Resultado"),
]