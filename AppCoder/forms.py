from django import forms


class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()
    
class ProfesorFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    email = forms.CharField()
    profesion = forms.CharField(max_length=30)

class EstudianteFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    email = forms.CharField()

class EntregableFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    fechaDeEntrega = forms.DateField()
    entregado = forms.BooleanField()