from django.shortcuts import render
from miClub import models
from miClub import forms

# Create your views here.
def inicio(request):

    return render(request,"miClub/inicio.html")

def directivos(request):

    return render(request,"miClub/directivos.html")

def socios(request):

    return render(request,"miClub/socios.html")

def disciplinas(request):

    return render(request,"miClub/disciplinas.html")

def cuota(request):

    return render(request,"miClub/cuota.html")

def altaSocioFormulario(request):
    
    if request.method == "POST":

        miFormulario = forms.AltaSocioForm(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data
            socio = models.Socios(nombre=informacion['nombre'], apellido=informacion['apellido'],
                                  n_socio=informacion['n_socio'],fecha_ingreso=informacion['fecha_ingreso'],
                                  email=informacion['email'])
            socio.save()

            return render(request, "miClub/inicio.html")
    
    else:
        miFormulario = forms.AltaSocioForm()

        return render(request,"miClub/altaSocio.html", {"miFormulario":miFormulario})

def buscarSocioFormulario(request):

    return render(request, "miClub/buscaSocio.html")

def buscar(request):

    socio = models.Socios.objects.filter(n_socio=request.GET['nº socio'])
    contexto = {"socios":socio.values()}

    return render(request,"miClub/resultadoSocio.html",contexto)
#socio.values()[0]['nombre']+' '+socio.values()[0]['apellido']
