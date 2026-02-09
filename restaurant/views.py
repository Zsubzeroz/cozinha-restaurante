from django.shortcuts import render, redirect, get_object_or_404
from .models import DishType, Cook, Dish, Ingredient
from .forms import DishTypeForm, CookForm, IngredientForm, DishForm


def home(request):
    return redirect('dish_type_list')


def dish_detail(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    return render(request, 'restaurant/dish_detail.html', {'dish': dish})


def dishtype_detail(request, pk):
    dishtype = get_object_or_404(DishType, pk=pk)
    return render(request, 'restaurant/dishtype_detail.html', {'dishtype': dishtype})


def cook_detail(request, pk):
    cook = get_object_or_404(Cook, pk=pk)
    return render(request, 'restaurant/cook_detail.html', {'cook': cook})


def dish_type_list(request):
    dish_types = DishType.objects.all()
    form = DishTypeForm()
    context = {
        'dish_types': dish_types,
        'form': form,
        'editing_dish_type': None
    }
    return render(request, 'restaurant/manage_dish_types.html', context)


def dish_type_create(request):
    if request.method == 'POST':
        form = DishTypeForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('dish_type_list')


def dish_type_update(request, pk):
    instance = get_object_or_404(DishType, pk=pk)
    if request.method == 'POST':
        form = DishTypeForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('dish_type_list')
    else:
        form = DishTypeForm(instance=instance)
    context = {
        'dish_types': DishType.objects.all(),
        'form': form,
        'editing_dish_type': instance
    }
    return render(request, 'restaurant/manage_dish_types.html', context)


def dish_type_delete(request, pk):
    instance = get_object_or_404(DishType, pk=pk)
    if request.method == 'POST':
        instance.delete()
    return redirect('dish_type_list')


def cook_list(request):
    return render(request, 'restaurant/cook_list.html', {'cooks': Cook.objects.all()})


def manage_cooks(request, pk=None, action=None):
    instance = get_object_or_404(Cook, pk=pk) if pk else None
    if request.method == 'POST':
        form = CookForm(request.POST, instance=instance)
        if form.is_valid():
            if pk and action == 'edit':
                cook = form.save(commit=False)
                password = form.cleaned_data.get('password')
                if password:
                    cook.set_password(password)
                cook.save()
                form.save_m2m()
            elif not pk:
                Cook.objects.create_user(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password'],
                    years_of_experience=form.cleaned_data['years_of_experience']
                )
            return redirect('cook_list')
    if action == 'delete' and pk:
        instance.delete()
        return redirect('cook_list')
    context = {
        'cooks': Cook.objects.all(),
        'editing_cook': instance if pk and action == 'edit' else None,
        'form': CookForm(instance=instance)
    }
    return render(request, 'restaurant/manage_cooks.html', context)


def ingredient_list(request):
    return render(request, 'restaurant/ingredient_list.html', {'ingredients': Ingredient.objects.all()})


def manage_ingredients(request, pk=None, action=None):
    instance = get_object_or_404(Ingredient, pk=pk) if pk else None
    if request.method == 'POST':
        form = IngredientForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('ingredient_list')
    if action == 'delete' and pk:
        instance.delete()
        return redirect('ingredient_list')
    context = {
        'ingredients': Ingredient.objects.all(),
        'editing_ingredient': instance if pk and action == 'edit' else None,
        'form': IngredientForm(instance=instance)
    }
    return render(request, 'restaurant/manage_ingredients.html', context)


def dish_list(request):
    return render(request, 'restaurant/dish_list.html', {'dishes': Dish.objects.all()})


def manage_dishes(request, pk=None, action=None):
    instance = get_object_or_404(Dish, pk=pk) if pk else None
    if request.method == 'POST':
        form = DishForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('dish_list')
    if action == 'delete' and pk:
        instance.delete()
        return redirect('dish_list')
    context = {
        'dishes': Dish.objects.all(),
        'dish_types': DishType.objects.all(),
        'cooks': Cook.objects.all(),
        'editing_dish': instance if pk and action == 'edit' else None,
        'form': DishForm(instance=instance)
    }
    return render(request, 'restaurant/manage_dishes.html', context)
