from django import forms

class Form_Paciente(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
   
class Form_Medico(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
   
class Form_Visita(forms.Form):
    fecha = forms.DateField()
    sede = forms.CharField(max_length=30)
