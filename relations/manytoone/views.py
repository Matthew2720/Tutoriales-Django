from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter,Article
from datetime import date
# Create your views here.
def create(request):
    reporter = Reporter(first_name="Juanjo",last_name="Ruiz",email="juanjo@demo.com")
    reporter.save()
    
    article1 = Article(headline="Articulo1", pub_date=date(2022,5,5),reporter=reporter)
    article2 = Article(headline="Articulo2", pub_date=date(2021,10,8),reporter=reporter)
    article3 = Article(headline="Articulo3", pub_date=date(2020,10,5),reporter=reporter)
    article1.save()
    article2.save()
    article3.save()
    
    #Consulta desde el muchos a uno
    # query = article1.reporter.first_name
    
    #Consulta desde el uno a muchos
    # query = reporter.article_set.all()
    query = len(query)
    return HttpResponse(query)