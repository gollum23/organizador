#encoding:utf-8
from django.forms import forms, ModelForm
from Doggi.models import cliente, producto, tareas

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
      

class ProductoForm(ModelForm):
    class Meta:
        model = Producto


class TareasForm(ModelForm):
    class Meta:
        model = Tareas


class ClienteForm(forms.Form):
	nombre_apellido = forms.Charfield(max_length=100)
	CI_RIF = forms.IntegerField()
	telefono = forms.IntegerField()
	direccion = forms.Charfield(widget=forms.Textarea)
	mail = forms.EmailField()


class ProductoForm(forms.Form):
	nombre = forms.Charfield(max_length=50)
	tipo_producto = forms.Charfield(max_length=10,
					widget=forms.Select(TIPO_CHOICE)
		)
	cantidad = forms.IntegerField()
	clave = forms.IntegerField()


class TareasForm(forms.Form):
	fecha = forms.Charfield(max_length=10)
	prioridad = forms.Charfield(max_length=1,
				widget=forms.Select(TIPO_CHOICE)
		)
	descripcion = forms.Charfield(widget=Textarea())
