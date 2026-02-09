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
    return redirect('dish_type_list')


def dish_type_update(request, pk):
    dish_type_instance = get_object_or_404(DishType, pk=pk)
    if request.method == 'POST':
        form = DishTypeForm(request.POST, instance=dish_type_instance)
        if form.is_valid():
            form.save()
            return redirect('dish_type_list')
    else:
        form = DishTypeForm(instance=dish_type_instance)

    context = {
        'dish_types': DishType.objects.all(),
        'form': form,
        'editing_dish_type': dish_type_instance
    }
    return render(request, 'restaurant/manage_dish_types.html', context)


def dish_type_delete(request, pk):
    dish_type_instance = get_object_or_404(DishType, pk=pk)
    if request.method == 'POST':
        dish_type_instance.delete()
    return redirect('dish_type_list')


def home(request):
    return redirect('dish_type_list')


def cook_list(request):
    cooks = Cook.objects.all()
    context = {'cooks': cooks}
    return render(request, 'restaurant/cook_list.html', context)


def cook_create(request):
    if request.method == 'POST':
        form = CookForm(request.POST)
        if form.is_valid():
            # Lógica crucial: usar create_user para contas de usuário
            Cook.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                years_of_experience=form.cleaned_data['years_of_experience']
            )
            return redirect('cook_list')
    else:
        form = CookForm()

    context = {
        'form': form,
        'editing_cook': None
    }
    return render(request, 'restaurant/manage_cooks.html', context)


def cook_update(request, pk):
    cook_instance = get_object_or_404(Cook, pk=pk)
    if request.method == 'POST':
        form = CookForm(request.POST, instance=cook_instance)
        if form.is_valid():
            cook_instance = form.save(commit=False)
            password = form.cleaned_data.get('password')
            if password:
                cook_instance.set_password(password)
            cook_instance.save()
            return redirect('cook_list')
    else:
        form = CookForm(instance=cook_instance)

    context = {
        'form': form,
        'editing_cook': cook_instance
    }
    return render(request, 'restaurant/manage_cooks.html', context)


def cook_delete(request, pk):
    cook_instance = get_object_or_404(Cook, pk=pk)
    if request.method == 'POST':
        cook_instance.delete()
    return redirect('cook_list')


def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    form = IngredientForm()
    context = {
        'ingredients': ingredients,
        'form': form,
        'editing_ingredient': None
    }
    return render(request, 'restaurant/manage_ingredients.html', context)


def ingredient_create(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingredient_list')
    return redirect('ingredient_list')


def ingredient_update(request, pk):
    ingredient_instance = get_object_or_404(Ingredient, pk=pk)
    if request.method == 'POST':
        form = IngredientForm(request.POST, instance=ingredient_instance)
        if form.is_valid():
            form.save()
            return redirect('ingredient_list')
    else:
        form = IngredientForm(instance=ingredient_instance)

    context = {
        'ingredients': Ingredient.objects.all(),
        'form': form,
        'editing_ingredient': ingredient_instance
    }
    return render(request, 'restaurant/manage_ingredients.html', context)


def ingredient_delete(request, pk):
    ingredient_instance = get_object_or_404(Ingredient, pk=pk)
    if request.method == 'POST':
        ingredient_instance.delete()
    return redirect('ingredient_list')


def dish_list(request):
    dishes = Dish.objects.all()
    context = {'dishes': dishes}
    return render(request, 'restaurant/dish_list.html', context)


def dish_create(request):
    if request.method == 'POST':
        form = DishForm(request.POST)
        if form.is_valid():
            dish_instance = form.save()
            cook_ids = form.cleaned_data.get('cooks')
            dish_instance.cooks.set(cook_ids)
            return redirect('dish_list')
    else:
        form = DishForm()

    dish_types = DishType.objects.all()
    cooks = Cook.objects.all()
    context = {
        'form': form,
        'dish_types': dish_types,
        'cooks': cooks,
        'editing_dish': None
    }
    return render(request, 'restaurant/manage_dishes.html', context)


def dish_update(request, pk):
    dish_instance = get_object_or_404(Dish, pk=pk)
    if request.method == 'POST':
        form = DishForm(request.POST, instance=dish_instance)
        if form.is_valid():
            dish_instance = form.save()
            cook_ids = form.cleaned_data.get('cooks')
            dish_instance.cooks.set(cook_ids)
            return redirect('dish_list')
    else:
        form = DishForm(instance=dish_instance)

    dish_types = DishType.objects.all()
    cooks = Cook.objects.all()
    context = {
        'form': form,
        'dish_types': dish_types,
        'cooks': cooks,
        'editing_dish': dish_instance
    }
    return render(request, 'restaurant/manage_dishes.html', context)


def dish_delete(request, pk):
    dish_instance = get_object_or_404(Dish, pk=pk)
    if request.method == 'POST':
        dish_instance.delete()
    return redirect('dish_list')
