from django.contrib.auth.models import AbstractUser
from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name="cook_set",
        related_query_name="cook",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="cook_set",
        related_query_name="cook",
    )
    years_of_experience = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE, related_name='dishes')
    cooks = models.ManyToManyField(Cook, related_name='dishes')
    ingredients = models.ManyToManyField(Ingredient, related_name='dishes')

    def __str__(self):
        return self.name


class DishIngredient(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        unique_together = ('dish', 'ingredient')
        verbose_name = "Ingrediente do Prato"
        verbose_name_plural = "Ingredientes dos Pratos"

    def __str__(self):
        return f"{self.ingredient.name} ({self.quantity}) para {self.dish.name}"
