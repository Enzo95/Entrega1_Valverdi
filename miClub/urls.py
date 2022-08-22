from django.urls import path
from miClub import views

urlpatterns = [
    path('', views.inicio, name = "Inicio"),
    path('directivos/', views.directivos, name = "Directivos"),
    path('socios/', views.socios, name = "Socios"),
    path('disciplinas/', views.disciplinas, name = "Disciplinas"),
    path('cuota/', views.cuota, name = "Cuota"),
]