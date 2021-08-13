from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from store.models import Product
from films.models import Genre

# Create your views here.
def say_hello(request):
    

    return render(request, 'hello.html')