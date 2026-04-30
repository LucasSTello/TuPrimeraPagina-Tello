from django.shortcuts import render, redirect, get_object_or_404
from .models import Moto, Piloto, Carrera
from .forms import MotoForm, PilotoForm, CarreraForm

# Página de inicio
def inicio(request):
    return render(request, 'motocross/index.html')

# Vistas de Moto
def lista_motos(request):
    motos = Moto.objects.all()
    return render(request, 'motocross/moto_list.html', {'motos': motos})

def crear_moto(request):
    if request.method == 'POST':
        form = MotoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_motos')
    else:
        form = MotoForm()
    return render(request, 'motocross/moto_form.html', {'form': form})

# Vistas de Piloto
def lista_pilotos(request):
    pilotos = Piloto.objects.all()
    return render(request, 'motocross/piloto_list.html', {'pilotos': pilotos})

def crear_piloto(request):
    if request.method == 'POST':
        form = PilotoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pilotos')
    else:
        form = PilotoForm()
    return render(request, 'motocross/piloto_form.html', {'form': form})

# Vistas de Carrera
def lista_carreras(request):
    carreras = Carrera.objects.all()
    return render(request, 'motocross/carrera_list.html', {'carreras': carreras})

def crear_carrera(request):
    if request.method == 'POST':
        form = CarreraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_carreras')
    else:
        form = CarreraForm()
    return render(request, 'motocross/carrera_form.html', {'form': form})

# Búsqueda
def buscar(request):
    query = request.GET.get('q', '')
    resultados_motos = []
    if query:
        resultados_motos = Moto.objects.filter(nombre__icontains=query) | Moto.objects.filter(modelo__icontains=query)
    
    return render(request, 'motocross/buscar.html', {'resultados_motos': resultados_motos, 'query': query})
