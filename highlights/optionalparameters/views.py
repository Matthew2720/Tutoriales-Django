from django.shortcuts import render
from django.http import HttpResponse

def optional(request,name = 'Nombre por defecto'):
    return render (request, 'optional.html',{'name':name})
