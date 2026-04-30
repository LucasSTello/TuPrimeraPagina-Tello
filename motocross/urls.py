from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    
    # Motos
    path('motos/', views.lista_motos, name='lista_motos'),
    path('motos/crear/', views.crear_moto, name='crear_moto'),
    
    # Pilotos
    path('pilotos/', views.lista_pilotos, name='lista_pilotos'),
    path('pilotos/crear/', views.crear_piloto, name='crear_piloto'),
    
    # Carreras
    path('carreras/', views.lista_carreras, name='lista_carreras'),
    path('carreras/crear/', views.crear_carrera, name='crear_carrera'),
    
    # Búsqueda
    path('buscar/', views.buscar, name='buscar'),
]
