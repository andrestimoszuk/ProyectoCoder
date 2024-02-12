from django.shortcuts import render
from AppCoder import forms, models
from django.http import HttpResponse

def inicio(request):
    return render(request, 'AppCoder/inicio.html')


def medico(request):
    if request.method == 'POST':
        formulario = forms.Form_Medico(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            medico = models.Medico(nombre=informacion["nombre"], apellido=informacion["apellido"])
            medico.save()
            return render(request, 'AppCoder/medico.html')
    else:
        formulario = forms.Form_Medico()
        contexto = {"formulario": formulario}
        return render(request, "AppCoder/medico.html", contexto)
    

def paciente(request):
    if request.method == 'POST':
        formulario = forms.Form_Paciente(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            paciente = models.Paciente(nombre=informacion["nombre"], apellido=informacion["apellido"])
            paciente.save()
            return render(request, 'AppCoder/paciente.html')
    else:
        formulario = forms.Form_Paciente()
        contexto = {"formulario": formulario}
        return render(request, "AppCoder/paciente.html", contexto)


def visita(request):
    if request.method == 'POST':
        formulario = forms.Form_Visita(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            visita = models.Visita(fecha=informacion["fecha"], sede=informacion["sede"])
            visita.save()
            return render(request, 'AppCoder/paciente.html')
    else:
        formulario = forms.Form_Visita()
        contexto = {"formulario": formulario}
        return render(request, "AppCoder/visita.html", contexto)

def busqueda(request):
    return render(request, "AppCoder/busqueda.html")

def resultado(request):
    #respuesta = f'Estoy buscando la {request.GET["sede"]}'
    #return HttpResponse(respuesta)
    
    if request.GET['sede']:
        sede = request.GET['sede']
        fechas = models.Visita.objects.filter(sede__icontains=sede)
        return render(request, 'AppCoder/resultado.html', {'fecha': fechas, 'sede': sede})
    else:
        respuesta = 'No enviaste datos.'

    # No olvidar from django.http import HttpResponse
    return HttpResponse(respuesta)