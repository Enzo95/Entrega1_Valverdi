from django.urls import path
from miClub import views

urlpatterns = [
    path('', views.inicio, name = "Inicio"),
]