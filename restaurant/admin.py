from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Dish, DishType, Cook, Ingredient, DishIngredient


class DishIngredientInline(admin.TabularInline):
    model = DishIngredient
    extra = 1


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "dish_type")
    search_fields = ("name",)
    inlines = [DishIngredientInline]


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = ("username", "first_name", "last_name", "email", "years_of_experience")
    fieldsets = UserAdmin.fieldsets + (
        (("Additional Info"), {"fields": ("years_of_experience",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (("Additional Info"), {"fields": ("years_of_experience",)}),
    )


admin.site.register(DishType)
admin.site.register(Ingredient)
admin.site.register(DishIngredient)
