from django import forms
from .models import Fruit, Eating

class FruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ('name', 'climate', 'description', 'growtime')

class EatingForm(forms.ModelForm):
    
    class Meta:
        model = Eating
        fields = ['date', 'meal']
        