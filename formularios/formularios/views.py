from django.shortcuts import render
from django.http import HttpResponse

def form(request):
    return render(request,'form.html',{})

def goal(request):
    if request.method != 'GET':
        return HttpResponse("El mensaje POST no esta soportado para esta ruta")
    
    name = request.GET['name']
    message = request.GET['message']
    return render(request,'success.html',{'name':name,'message':message})

def postform(request):
    return render(request,'post/postform.html',{})

def postgoal(request):
    if request.method != 'POST':
        return HttpResponse("El mensaje POST no esta soportado para esta ruta")
    
    name = request.POST['name']
    message = request.POST['message']
    return render(request,'postgoal.html',{'name':name,'message':message})