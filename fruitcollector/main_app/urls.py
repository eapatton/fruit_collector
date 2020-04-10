from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('fruits/', views.fruits_index, name='index'),
    path('fruits/<int:fruit_id>/', views.fruits_detail, name='detail'),
]