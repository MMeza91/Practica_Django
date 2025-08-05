from django.shortcuts import render

# Create your views here.
def home(request):
    contexto = {}
    return render(request, 'home.html', contexto)

def test(request, variable):
    contexto = {'variable':variable}
    return render(request, 'test.html', contexto)