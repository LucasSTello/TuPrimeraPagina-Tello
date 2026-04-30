from django import forms
from .models import Moto, Piloto, Carrera

class MotoForm(forms.ModelForm):
    class Meta:
        model = Moto
        fields = ['nombre', 'modelo', 'anio', 'cilindrada', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'anio': forms.NumberInput(attrs={'class': 'form-control'}),
            'cilindrada': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class PilotoForm(forms.ModelForm):
    class Meta:
        model = Piloto
        fields = ['nombre', 'edad', 'nacionalidad', 'moto']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'nacionalidad': forms.TextInput(attrs={'class': 'form-control'}),
            'moto': forms.Select(attrs={'class': 'form-select'}),
        }

class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = ['nombre_evento', 'ubicacion', 'fecha', 'piloto_ganador']
        widgets = {
            'nombre_evento': forms.TextInput(attrs={'class': 'form-control'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'piloto_ganador': forms.Select(attrs={'class': 'form-select'}),
        }
