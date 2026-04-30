from django.db import models

class Moto(models.Model):
    nombre = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    anio = models.IntegerField()
    cilindrada = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.modelo} ({self.anio})"

class Piloto(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    nacionalidad = models.CharField(max_length=100)
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, related_name='pilotos')

    def __str__(self):
        return f"{self.nombre} ({self.nacionalidad})"

class Carrera(models.Model):
    nombre_evento = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=200)
    fecha = models.DateField()
    piloto_ganador = models.ForeignKey(Piloto, on_delete=models.SET_NULL, null=True, blank=True, related_name='victorias')

    def __str__(self):
        return f"{self.nombre_evento} - {self.fecha}"
