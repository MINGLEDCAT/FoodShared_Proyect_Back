from django.db import models

class Alimentos(models.Model):
    nombre_alimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    unidad_de_medida = models.CharField(max_length=10, choices=[('kg', 'kg'), ('unidad', 'unidad'), ('litros', 'litros'), ('cajas', 'cajas')])
    fecha_vencimiento = models.DateField()
    condicion = models.CharField(max_length=10, choices=[('Buen estado', 'Buen estado'), ('Mal estado', 'Mal estado')])
    existencia_producto = models.CharField(max_length=10, choices=[('Disponible', 'Disponible'), ('Reservado', 'Reservado'), ('Donado', 'Donado')])

    def __str__(self):
        return self.nombre_alimento
