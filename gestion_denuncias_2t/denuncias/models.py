from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

# Categorias predefinidas

CATEGORIAS = [
    ('bache', 'Bache'),
    ('alumbrado', 'Alumbrado'),
    ('basura', 'Basura'),
    ('otro', 'Otro'),
]

# Modelo de Denuncia
class Denuncia(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='Título')
    descripcion = models.TextField(verbose_name='Descripción')
    imagen = models.ImageField(upload_to='media', verbose_name='Imagen')
    categoria = models.CharField(
        max_length=50,
        choices=CATEGORIAS,
        verbose_name='Categoría'
    )
    estado = models.CharField(
        max_length=50,
        choices=[('pendiente', 'Pendiente'), ('resuelto', 'Resuelto')],
        default='pendiente',
        verbose_name='Estado'
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo