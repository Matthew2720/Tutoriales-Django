from django.shortcuts import render
from .forms import ProductForm
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method == 'POST':
        #Guardar
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            productName = request.POST['name']
            return render(request,'index.html',{'form':form,'productName' : productName})
        else:
            return HttpResponse("Ingreso un dato no valido")
    else:
        form = ProductForm
        return render(request,'index.html',{'form':form})