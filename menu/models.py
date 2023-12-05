from django.db import models

# Create your models here.
class Bebida(models.Model):
    nombre = models.CharField(max_length=100)
    ingredientes = models.TextField(null=True, blank=True)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to= "bebida/imagen", null=True, blank=True)
    alcohol = models.BooleanField(default=False)
    disponible = models.BooleanField(default=False)
    
    
    def __srt__(self):
        return self.nombre   
    
class Comida(models.Model):
    nombre = models.CharField(max_length=100)
    ingredientes = models.TextField(null=True, blank=True)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to= "comida/imagen", null=True, blank=True)
    disponible = models.BooleanField(default=False)
    
    
    def __srt__(self):
        return self.nombre
    
    
    