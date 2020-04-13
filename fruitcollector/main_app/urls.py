from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('fruits/', views.fruits_index, name='index'),
    path('fruits/new/', views.new_fruit, name= 'new_fruit'),
    # path('fruits/create/', views.FruitCreate.as_view(), name='fruits_create'),
    path('fruits/<int:fruit_id>/', views.fruits_detail, name='detail'),
    path('fruits/<int:fruit_id>/add_eating/', views.add_eating, name='add_eating'),
    path('fruits/<int:fruit_id>/assoc_recipe/<int:recipe_id>/', views.assoc_recipe, name='assoc_recipe'),

    path('recipes/', views.RecipeList.as_view(), name='recipes_index'),
    path('recipes/<int:pk>/', views.RecipeDetail.as_view(), name='recipes_detail'),
    path('recipes/create/', views.RecipeCreate.as_view(), name='recipes_create'),
    path('recipes/<int:pk>/update/', views.RecipeUpdate.as_view(), name='recipes_update'),
    path('recipes/<int:pk>/delete/', views.RecipeDelete.as_view(), name='recipes_delete'),
    path('accounts/signup', views.signup, name='signup'),
]