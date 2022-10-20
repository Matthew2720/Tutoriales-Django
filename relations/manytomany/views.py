from django.shortcuts import render
from django.http import HttpResponse
from .models import Article,Publication
# Create your views here.
def create(request):
    #PRIMERO SE CREAN LOS ELEMENTOS Y LUEGO SE RELACIONAN
    publication = Publication(title="Publicacion1")
    publication.save()
    publication2 = Publication(title="Publicacion2")
    publication2.save()
    publication3 = Publication(title="Publicacion3")
    publication3.save()
    publication4 = Publication(title="Publicacion4")
    publication4.save()
    publication5 = Publication(title="Publicacion5")
    publication5.save()
    publication6 = Publication(title="Publicacion6")
    publication6.save()
    publication7 = Publication(title="Publicacion7")
    publication7.save()
    
    article = Article(headline="Articulo1")
    article.save()
    article2 = Article(headline="Articulo2")
    article2.save()
    article3 = Article(headline="Articulo3")
    article3.save()
    
    #Relaciones
    article.publications.add(publication)
    article.publications.add(publication2)
    article.publications.add(publication3)
    
    article2.publications.add(publication4)
    article2.publications.add(publication5)
    article2.publications.add(publication6)
    
    article3.publications.add(publication2)
    article3.publications.add(publication3)
    article3.publications.add(publication7)
    
    #Busquedas camino derecho
    resultado=article3.publications.all()
    
    #Busqueda camino contrario
    pub1 = Publication.objects.get(id=2)
    resultado=pub1.article_set.all()
    
    #Para eliminar relacion seria
    #article.publications.remove(publication)
    return HttpResponse(resultado)