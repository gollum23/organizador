#encoding:utf-8
from django.db import models


class Cliente(models.Model):
    nombre_apellido = models.CharField(max_length=100)
    CI_RIF = models.IntegerField()
    telefono = models.IntegerField()
    direccion = models.TextField(
        verbose_name='Dirección',
        help_text='Introduce la dirección del cliente'
    )
    mail = models.EmailField(max_length=75)

    def __unicode__(self):
        return self.nombre_apellido


class Producto(models.Model):
    indx = models.ForeignKey('cliente')
    nombre = models.TextField(max_length=50)
    TIPO_COHICE = (
        ('MN2000', 'Control MN2000'),
        ('DG2', 'Control Unik DG2'),
        ('DG1', 'Control Unik DG1'),
        ('ICARO', 'Motor Icaro'),
    )
    tipo = models.CharField(max_length=10, choices=TIPO_COHICE)
    cantidad = models.IntegerField()
    clave = models.IntegerField()

    def __unicode__(self):
        return self.nombre


class Tareas(models.Model):
    indx = models.ForeignKey('cliente')
    fecha = models.CharField(max_length=10)
    PRIORIDAD_CHOICE = (
        ('U', 'Urgente'),
        ('I', 'Importante'),
        ('N', 'Normal'),
        ('B', 'Baja'),
    )
    prioridad = models.CharField(max_length=1, choices=PRIORIDAD_CHOICE)
    descripcion = models.TextField(verbose_name='Descripción')

    def __unicode__(self):
        return self.fecha
