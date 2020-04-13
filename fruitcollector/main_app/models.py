from django.db import models
from django.urls import reverse
from datetime import date

from django.contrib.auth.models import User

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    time = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("recipes_detail", kwargs={"pk": self.id})
        
class Fruit(models.Model):
    name = models.CharField(max_length=100)
    climate = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    growtime = models.IntegerField()
    recipes = models.ManyToManyField(Recipe)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def ate_for_today(self):
        return self.eating_set.filter(date=date.today()).count() >= len(MEALS)    
    
class Eating(models.Model):
    date = models.DateField('Eating Date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )
    fruit = models.ForeignKey(Fruit, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
    