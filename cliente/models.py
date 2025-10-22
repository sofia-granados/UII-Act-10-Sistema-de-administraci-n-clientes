from django.db import models

# Create your models here.
class Cliente(models.Model):
    apepaterno = models.CharField(max_length=100)
    apematerno = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    domicilio = models.TextField()
    correo_electronico = models.EmailField()
    telefono = models.CharField(max_length=15)
    alergias = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.nombre} {self.apepaterno} {self.apematerno}'