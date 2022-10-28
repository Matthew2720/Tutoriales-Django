from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='contact'),
    path("view/<int:id>",views.view,name="view"),
    path("edit/<int:id>",views.edit,name="edit"),
    path("create",views.create,name='create'),
    path("delete/<int:id>",views.delete,name='delete')
]