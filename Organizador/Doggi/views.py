from django.shortcuts import render_to_response
from Doggi.models import Cliente, Producto, Tareas


def vista_general(request):
    clientes = Cliente.objects.all()
    return render_to_response('inicio.html', {'cliente': clientes})


def cliente(request):
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()
    tarea = Tareas.objects.all()
    return render_to_response(
        'cliente.html',
        {'cliente': clientes,
        'producto': productos,
        'tarea': tareas}
    )
