from django.contrib import admin
from .models import Product

class ProductAdmin (admin.ModelAdmin):
    list_display = ('name','short_description', 'stock',)#Añadir como se visualiza la informacion y campos
    search_fields = ('name','short_description',) #campo de busqueda
    list_filter = ('stock','discount_until')  #filtros
    date_hierarchy = "discount_until" #jerarquia

admin.site.register(Product, ProductAdmin)


# Register your models here.
