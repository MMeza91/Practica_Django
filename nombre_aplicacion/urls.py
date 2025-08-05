from django.urls import path
from .views import home, test

urlpatterns = [
    path('home/', home, name='home'),
    path('test/<str:variable>/', test, name='test'), #esta ruta se escribira en el navegador y lo que se coloque será la variable que después de utilice
    
]