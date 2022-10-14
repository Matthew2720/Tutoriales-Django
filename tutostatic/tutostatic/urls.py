from django.contrib import admin
from django.urls import path
from tutostatic.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("estaticos/",estaticos, name='estaticos'),
]
