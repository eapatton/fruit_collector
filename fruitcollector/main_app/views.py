from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Fruit, Recipe
from .forms import FruitForm, EatingForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')    

@login_required
def fruits_index(request):
    fruits = Fruit.objects.filter(user=request.user)
    return render(request, 'fruits/index.html', { 'fruits': fruits})

def fruits_detail(request, fruit_id):
    fruit = Fruit.objects.get(id = fruit_id)
    recipes_fruit_doesnt_have = Recipe.objects.exclude(id__in = fruit.recipes.all().values_list('id'))
    eating_form = EatingForm()
    context = {
        'fruit' : fruit, 
        'eating_form': eating_form,
        'recipes': recipes_fruit_doesnt_have
        }
    return render(request, 'fruits/detail.html', context)

def add_eating(request, fruit_id):
    form = EatingForm(request.POST)

    if form.is_valid():
        new_eating = form.save(commit=False)
        new_eating.fruit_id = fruit_id
        new_eating.save()
    return redirect('detail', fruit_id=fruit_id)

def assoc_recipe(request, fruit_id, recipe_id):
    Fruit.objects.get(id=fruit_id).recipes.add(recipe_id)
    return redirect('detail', fruit_id=fruit_id)

def new_fruit(request):
    if request.method == 'POST':
        form = FruitForm(request.POST)
        if form.is_valid():
            fruit = form.save(commit=False)
            fruit.user = request.user
            fruit.save()
            return redirect('detail', fruit.id)
    else:
        form = FruitForm()
    context = { 'form': form}
    return render(request, 'fruits/fruit_form.html', context)        



def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class RecipeList(LoginRequiredMixin, ListView):
    model = Recipe

class RecipeDetail(LoginRequiredMixin, DetailView):
    model = Recipe    

class RecipeCreate(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = '__all__'

class RecipeUpdate(LoginRequiredMixin, UpdateView):
    model = Recipe
    fields = ['name', 'description', 'time']

class RecipeDelete(LoginRequiredMixin, DeleteView):
    model = Recipe
    success_url = '/recipes/'    