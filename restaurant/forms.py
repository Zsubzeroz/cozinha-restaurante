from django import forms
from .models import DishType, Cook, Ingredient, Dish

class DishTypeForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = ['name']

class CookForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = Cook
        fields = ['username', 'email', 'years_of_experience']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name']

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'description', 'price', 'dish_type', 'cooks']
