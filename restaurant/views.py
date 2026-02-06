from django.shortcuts import render, redirect, get_object_or_404
from .models import DishType, Cook, Dish, Ingredient
from .forms import DishTypeForm, CookForm, IngredientForm, DishForm


def dish_detail(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    context = {'dish': dish}
    return render(request, 'restaurant/dish_detail.html', context)


def dishtype_detail(request, pk):
    dishtype = get_object_or_404(DishType, pk=pk)
    context = {'dishtype': dishtype}
    return render(request, 'restaurant/dishtype_detail.html', context)


def cook_detail(request, pk):
    cook = get_object_or_404(Cook, pk=pk)
    context = {'cook': cook}
    return render(request, 'restaurant/cook_detail.html', context)



def home(request):
    return redirect('manage_dish_types')


def manage_dish_types(request, pk=None, action=None):
    dish_type_instance = None

    if pk:
        dish_type_instance = get_object_or_404(DishType, pk=pk)

    if request.method == 'POST':
        form = DishTypeForm(request.POST, instance=dish_type_instance)
        if form.is_valid():
            form.save()
            return redirect('manage_dish_types')

    elif action == 'delete' and pk:
        dish_type_instance.delete()
        return redirect('manage_dish_types')

    dish_types = DishType.objects.all()
    form = DishTypeForm(instance=dish_type_instance)

    context = {
        'dish_types': dish_types,
        'editing_dish_type': dish_type_instance if pk and action == 'edit' else None,
        'form': form
    }
    return render(request, 'restaurant/manage_dish_types.html', context)



def cook_list(request):
    cooks = Cook.objects.all()
    context = {'cooks': cooks}
    return render(request, 'restaurant/cook_list.html', context)


def manage_cooks(request, pk=None, action=None):
    cook_instance = None

    if pk:
        cook_instance = get_object_or_404(Cook, pk=pk)

    if request.method == 'POST':
        form = CookForm(request.POST, instance=cook_instance)

        if form.is_valid():
            if pk and action == 'edit':  # UPDATE
                cook_instance = form.save(commit=False)

                password = form.cleaned_data.get('password')
                if password:
                    cook_instance.set_password(password)

                cook_instance.save()
                return redirect('cook_list')

            elif not pk:  # CREATE
                user = Cook.objects.create_user(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password'],
                    years_of_experience=form.cleaned_data['years_of_experience']
                )
                return redirect('cook_list')

    if action == 'delete' and pk:
        cook_instance.delete()
        return redirect('cook_list')

    form = CookForm(instance=cook_instance)
    cooks = Cook.objects.all()

    context = {
        'cooks': cooks,
        'editing_cook': cook_instance if pk and action == 'edit' else None,
        'form': form
    }
    return render(request, 'restaurant/manage_cooks.html', context)



def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    context = {'ingredients': ingredients}
    return render(request, 'restaurant/ingredient_list.html', context)


def manage_ingredients(request, pk=None, action=None):
    ingredient_instance = None

    if pk:
        ingredient_instance = get_object_or_404(Ingredient, pk=pk)

    if request.method == 'POST':
        form = IngredientForm(request.POST, instance=ingredient_instance)
        if form.is_valid():
            form.save()
            return redirect('ingredient_list')

    if action == 'delete' and pk:
        ingredient_instance.delete()
        return redirect('ingredient_list')

    ingredients = Ingredient.objects.all()
    form = IngredientForm(instance=ingredient_instance)

    context = {
        'ingredients': ingredients,
        'editing_ingredient': ingredient_instance if pk and action == 'edit' else None,
        'form': form
    }
    return render(request, 'restaurant/manage_ingredients.html', context)



def dish_list(request):
    dishes = Dish.objects.all()
    context = {'dishes': dishes}
    return render(request, 'restaurant/dish_list.html', context)


def manage_dishes(request, pk=None, action=None):
    dish_instance = None

    if pk:
        dish_instance = get_object_or_404(Dish, pk=pk)

    if request.method == 'POST':
        form = DishForm(request.POST, instance=dish_instance)
        if form.is_valid():
            dish_instance = form.save()
            return redirect('dish_list')

    if action == 'delete' and pk:
        dish_instance.delete()
        return redirect('dish_list')

    dish_types = DishType.objects.all()
    cooks = Cook.objects.all()

    form = DishForm(instance=dish_instance)

    context = {
        'dishes': Dish.objects.all(),
        'dish_types': dish_types,
        'cooks': cooks,
        'editing_dish': dish_instance if pk and action == 'edit' else None,
        'form': form
    }
    return render(request, 'restaurant/manage_dishes.html', context)
