from django.shortcuts import render
from .forms import PlaceForm
# Create your views here.
def index(request):
    form = PlaceForm
    return render(request,'index.html',{'form':form})
