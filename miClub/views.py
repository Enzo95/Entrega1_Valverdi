from django.shortcuts import render
from django.http import HttpResponse
from miClub import models

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