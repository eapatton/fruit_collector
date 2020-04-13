from django.contrib import admin

from .models import Fruit, Eating, Recipe
# Register your models here.
admin.site.register(Fruit)
admin.site.register(Eating)
admin.site.register(Recipe)
