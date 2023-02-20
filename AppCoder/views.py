from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import CursoFormulario, ProfesorFormulario, EntregableFormulario, EstudianteFormulario
#from django.views.generic import ListView
#from django.views.generic.detail import DetailView
#from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def inicio(request):
    return render(request, 'AppCoder/inicio.html')
    #return HttpResponse('vista inicio')

#def profesores(request):
    #return render(request, 'AppCoder/profesores.html')

#def estudiantes(request):
    #return render(request, 'AppCoder/estudiantes.html')
    #return HttpResponse('vista estudiantes')

#def entregables(request):
    #return render(request, 'AppCoder/entregables.html')
    #return HttpResponse('vista entregables')

def cursos(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion['curso'], camada=informacion['camada'])
            curso.save()
            return render(request, "AppCoder/inicio.html")

    else:
        miFormulario= CursoFormulario()
    
    return render(request, "AppCoder/cursoFormulario.html", {"miFormulario": miFormulario})

def profesores(request):
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], profesion=informacion['profesion'])
            profesor.save()
            return render(request, "AppCoder/inicio.html")

    else:
        miFormulario= ProfesorFormulario()
    
    return render(request, "AppCoder/profesorFormulario.html", {"miFormulario": miFormulario})

def estudiantes(request):
    if request.method == 'POST':
        miFormulario = EstudianteFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            estudiante = Estudiante(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])
            estudiante.save()
            return render(request, "AppCoder/inicio.html")

    else:
        miFormulario= EstudianteFormulario()
    
    return render(request, "AppCoder/estudianteFormulario.html", {"miFormulario": miFormulario})

def entregables(request):
    if request.method == 'POST':
        miFormulario = EntregableFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            entregable = Entregable(nombre=informacion['nombre'], fechaDeEntrega=informacion['fechaDeEntrega'], entregado=informacion['entregado'])
            entregable.save()
            return render(request, "AppCoder/inicio.html")

    else:
        miFormulario= EntregableFormulario()
    
    return render(request, "AppCoder/entregableFormulario.html", {"miFormulario": miFormulario})

def busquedaCamada(request):
    return render(request, "AppCoder/busquedaCamada.html")

def buscar(request):
    if request.GET["camada"]:
        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada__icontains=camada)
        return render(request, "AppCoder/resultadoBusqueda.html", {"cursos":cursos, "camada":camada})

    else:
        respuesta= "No enviaste datos"
    
    return HttpResponse(respuesta)

    
def busquedaProfesor(request):
    return render(request, "AppCoder/busquedaProfesor.html")

def buscarProfesor(request):
    if request.GET["profesion"]:
        profesion = request.GET['profesion']
        profesiones = Profesor.objects.filter(profesion__icontains=profesion)
        return render(request, "AppCoder/resultadoProfesor.html", {"profesiones":profesiones, "profesion":profesion})

    else:
        respuesta= "No enviaste datos"
    
    return HttpResponse(respuesta)