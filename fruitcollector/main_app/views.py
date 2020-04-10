from django.shortcuts import render
from .models import Fruit

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')    

def fruits_index(request):
    fruits = Fruit.objects.all()
    return render(request, 'fruits/index.html', { 'fruits': fruits})

def fruits_detail(request, fruit_id):
    fruit = Fruit.objects.get(id = fruit_id)
    return render(request, 'fruits/detail.html', {'fruit' : fruit} )