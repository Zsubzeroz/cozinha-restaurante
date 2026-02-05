from django.db import models

class DishType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Cook(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    years_of_experience = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE, related_name='dishes')
    cooks = models.ManyToManyField(Cook, related_name='dishes_prepared')

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class DishIngredient(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50)

    class Meta:
        unique_together = ('dish', 'ingredient')
        verbose_name_plural = "Dish Ingredients"

    def __str__(self):
        return f"{self.dish.name} - {self.ingredient.name}"
