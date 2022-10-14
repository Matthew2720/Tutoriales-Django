from django.shortcuts import render

def base(request):
    contexto = {}
    return render(request,'base.html',contexto)

def herencia2(request):
    contexto = {}
    return render(request,'herencia2.html',contexto)

def index(request):
    return render(request,'index.html',{})

def prueba(request):
    return render(request,'prueba.html',{})
