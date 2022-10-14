from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment
# Create your views here.
def test(request):
    return HttpResponse("Funciona correctamente")

def create(request):
#1 METODO DE CREACION    
    # comment = Comment(name="Juanjo",score="5",comment="Este es un comentario")
    # comment.save() # Guardar en la base
    
#2 METODO
    #comment = Comment.objects.create(name="alex")
    return HttpResponse("Ruta para probar la creacion de modelos")

def delete(request):
#METODO DE ELIMINACION #1
    # comment = Comment.objects.get(id=1)
    # comment.delete()
#metodo de eliminacion #2, ruta directa
    # Comment.objects.filter(id=2).delete()
    return HttpResponse("Ruta para probar los borrados")