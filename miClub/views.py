from django.shortcuts import render
from django.http import HttpResponse
from miClub import models

# Create your views here.
def inicio(request):

    return render(request,"miClub/inicio.html")