from operator import index
from django.contrib import admin
from django.urls import path
from Herencia.views import *
urlpatterns = [
    path("admin/", admin.site.urls),
    path("base/",base,name="herencia"),
    path("herencia2/",herencia2,name="herencia2"),
    path("",index,name="index"),
    path("prueba/",prueba,name="prueba"),
]
