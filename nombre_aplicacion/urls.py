from django.urls import path
from .views import home, test, listar_productos, ProductoCreateView, ProductoDeleteView, ProductoDetailView, ProductoListView, ProductoUpdateView

urlpatterns = [
    path('home/', home, name='home'),
    path('test/<str:variable>/', test, name='test'), #esta ruta se escribira en el navegador y lo que se coloque será la variable que después de utilice
    path("productos/", listar_productos, name="lista_productos"),
    path("crear/",ProductoCreateView.as_view(),name="crear_productos"),
    path("",ProductoListView.as_view(),name="lista_productos"),
    path("producto/<int:pk>",ProductoDetailView.as_view(),name="detalle_producto"),
    path("producto/actualizacion/<int:pk>",ProductoUpdateView.as_view(),name="actualizar_producto"),
    path("producto/borrar/<int:pk>",ProductoDeleteView.as_view(),name="borrar_producto")
    
    
]
#path("",,name=""),