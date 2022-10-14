from django.shortcuts import render

def estaticos(request):
    contextos = {}
    return render(request,'estaticos.html',contextos)