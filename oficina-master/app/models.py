from django.db import models
from django.contrib.auth.models import User, AbstractUser
import json

# Create your models here.

TIPOS_USUARIO = (
	('Jefactura ISC','Jefactura ISC'),
	('Secretaria','Secretaria'),
    ('Jefactura de Docencia', 'Jefactura de Docencia'),
    ('Jefactura de Vinculacion', 'Jefactura de Vinculacion'),
    ('Jefactura de Investigacion', 'Jefactura de Investigacion'),
    ('Jefactura de Laboratorio', 'Jefactura de Laboratorio'),
    ('Docentes', 'Docentes'),
)

class Usuarios(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100, choices=TIPOS_USUARIO)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.usuario.username


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    link = models.URLField(verbose_name="Dirección Web", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "comunicado"
        verbose_name_plural = "comunicados"
        ordering = ["-created"]

    def __str__(self):
        return self.title