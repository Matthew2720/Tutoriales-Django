from django.forms import ModelForm
from .models import *

class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = '__all__'