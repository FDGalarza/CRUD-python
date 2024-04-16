from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm

# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

# View that show the  books list
def libros(request):
    # Get informatión of model Libros
    libros = Libro.objects.all()
    # {"libros": libros} sent the books list at view
    return render(request, 'libros/index.html', {"libros": libros})

# View that show the screen of create books
def create(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('index')
    return render(request, 'libros/create.html', {'formulario': formulario})

# View that show the screen of update books
def update(request, id):
    libro = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    #valida si se modifico el registro
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('index')
    return render(request, 'libros/update.html', {'formulario': formulario})

# Vies para eliminar libro
def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('index')


#ReCUPERAR DATOS A EDITAR 2:10