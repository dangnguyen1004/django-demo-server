from django.shortcuts import render
from django.http import HttpResponse
from films.models import Genre, Film

# Create your views here.
def welcome(request):
    

    return render(request, 'index.html')

def getAllFilms(request):
    query_set = Film.objects.all()
    list(query_set)

    return render(request, 'index.html')