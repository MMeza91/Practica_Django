from django.shortcuts import render
from .models import Producto

# Create your views here.
def home(request):
    contexto = {}
    return render(request, 'home.html', contexto)

def test(request, variable):
    contexto = {'variable':variable} #utiliza la variable ingresada en la url dentro del html
    return render(request, 'test.html', contexto)

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, "lista_de_productos.html",{"productos": productos})