from django.http import HttpResponse
from django.shortcuts import render
from .models import Author,Entry

# Create your views here.
def queries(request):
    # 1. Obtener todos los elementos
    authors = Author.objects.all()
    
    # 2.Obtener datos filtrados por condiciones
    filtered = Author.objects.filter(email ='danaharris@example.com')
    
    # 3.Obtener un unico objeto(filtrado)
    filterone = Author.objects.get(id=1)
    
    # 4.Obtener limitado a 10 elementos
    limit = Author.objects.all()[:10]
    
    # 5.Obtener 10 valores saltando los 5 primeros
    offset = Author.objects.all()[5:15]
    
    # 6.Ordenar elementos
    orders = Author.objects.all().order_by('email')
    
    # 7. Todos los elementos cuyo id sea <= 15
    #Modificadores
    #__lte = (<=) ; __gte = (>=) ; __lt = (<) ; __gt = (>); __contains = contiene; __exact = exacto
    rango = Author.objects.filter(id__lte=15)
    
    #8 Obtener todos los autores que cotienen en su nombre la palabras 'yes'
    contains = Author.objects.filter(name__contains='My')
    
    return render(request,"post/queries.html", {'authors':authors, 'filtered' : filtered, 'filterone':filterone, 'limit' : limit, 'offset' : offset, 'orders': orders,'rango':rango, 'contains':contains})

def update(request):
    author = Author.objects.get(id = 1)
    author.name = "Juanjo"
    author.email = "juanjo@demo.com"
    author.save()
    return HttpResponse("Modificado")