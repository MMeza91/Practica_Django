from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Producto
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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




class ProductoListView(ListView):
    model = Producto
    template_name = "productos/lista_productos.html"
    context_object_name = "productos"

class ProductoDetailView(DetailView) :
    model = Producto
    template_name = "productos/detalle_productos.html"
    context_object_name = "producto"

class ProductoCreateView(CreateView):
    model = Producto
    template_name = "productos/formulario_productos.html"
    field = ['nombre','descripcion','precio','stock','imagen']
    success_url = reverse_lazy("lista_productos")

class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = "productos/formulario_productos.html"
    field = ['nombre','descripcion','precio','stock','imagen']
    success_url = reverse_lazy("lista_productos")

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = "productos/confirma_productos.html"
    success_url = reverse_lazy("lista_productos")