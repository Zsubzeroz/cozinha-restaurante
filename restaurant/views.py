from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import DishType, Cook, Dish, Ingredient


# --- Views para DishType (CRUD Completo Implementado) ---

def home(request):
    return redirect('manage_dish_types')


def manage_dish_types(request, pk=None, action=None):
    dish_type_instance = None

    if pk:
        dish_type_instance = get_object_or_404(DishType, pk=pk)

    if request.method == 'POST':
        name = request.POST.get('name')

        if pk and action == 'edit':  # UPDATE
            dish_type_instance.name = name
            dish_type_instance.save()
            return redirect('manage_dish_types')
        elif not pk:  # CREATE
            if name:
                DishType.objects.create(name=name)
                return redirect('manage_dish_types')

    if action == 'delete' and pk:
        dish_type_instance.delete()
        return redirect('manage_dish_types')

    # GET (Listagem e Formulário de Criação/Edição)
    dish_types = DishType.objects.all()

    context = {
        'dish_types': dish_types,
        'editing_dish_type': dish_type_instance if pk and action == 'edit' else None
    }
    return render(request, 'restaurant/manage_dish_types.html', context)


# --- Views para Cook (Cozinheiro) ---

def cook_list(request):
    cooks = Cook.objects.all()
    context = {'cooks': cooks}
    return render(request, 'restaurant/cook_list.html', context)


def manage_cooks(request, pk=None, action=None):
    cook_instance = None

    if pk:
        cook_instance = get_object_or_404(Cook, pk=pk)

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        years_of_experience = request.POST.get('years_of_experience')
        # Se for edição e a senha for passada, defina a nova senha
        password = request.POST.get('password')

        if pk and action == 'edit':  # UPDATE
            cook_instance.username = username
            cook_instance.email = email
            cook_instance.years_of_experience = years_of_experience
            if password:  # Só atualiza a senha se ela foi enviada
                cook_instance.set_password(password)
            cook_instance.save()
            return redirect('cook_list')
        elif not pk:  # CREATE
            if username and email:
                # Use create_user para gerar a senha de forma segura
                Cook.objects.create_user(username=username, email=email, password=password or 'defaultpassword',
                                         years_of_experience=years_of_experience)
                return redirect('cook_list')

    if action == 'delete' and pk:
        cook_instance.delete()
        return redirect('cook_list')

    # GET (Listagem e Formulário de Criação/Edição)
    cooks = Cook.objects.all()

    context = {
        'cooks': cooks,
        'editing_cook': cook_instance if pk and action == 'edit' else None
    }
    return render(request, 'restaurant/manage_cooks.html', context)


# --- Views para Ingredient (Ingrediente - Opcional) ---

def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    context = {'ingredients': ingredients}
    return render(request, 'restaurant/ingredient_list.html', context)


def manage_ingredients(request, pk=None, action=None):
    ingredient_instance = None

    if pk:
        ingredient_instance = get_object_or_404(Ingredient, pk=pk)

    if request.method == 'POST':
        name = request.POST.get('name')

        if pk and action == 'edit':
            ingredient_instance.name = name
            ingredient_instance.save()
            return redirect('ingredient_list')
        elif not pk:
            if name:
                Ingredient.objects.create(name=name)
                return redirect('ingredient_list')

    if action == 'delete' and pk:
        ingredient_instance.delete()
        return redirect('ingredient_list')

    ingredients = Ingredient.objects.all()

    context = {
        'ingredients': ingredients,
        'editing_ingredient': ingredient_instance if pk and action == 'edit' else None
    }
    return render(request, 'restaurant/manage_ingredients.html', context)


# --- Views para Dish (Prato) ---

def dish_list(request):
    dishes = Dish.objects.all()
    context = {'dishes': dishes}
    return render(request, 'restaurant/dish_list.html', context)


def manage_dishes(request, pk=None, action=None):
    dish_instance = None

    if pk:
        dish_instance = get_object_or_404(Dish, pk=pk)

    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        dish_type_id = request.POST.get('dish_type')
        cook_ids = request.POST.getlist('cooks')

        if pk and action == 'edit':
            dish_instance.name = name
            dish_instance.description = description
            dish_instance.price = price
            dish_instance.dish_type_id = dish_type_id
            dish_instance.save()
            dish_instance.cooks.set(cook_ids)  # O .set() deve funcionar em tempo de execução
            return redirect('dish_list')

        elif not pk:  # CREATE
            if name and dish_type_id:
                new_dish = Dish.objects.create(
                    name=name,
                    description=description,
                    price=price,
                    dish_type_id=dish_type_id
                )
                new_dish.cooks.set(cook_ids)
                return redirect('dish_list')

    if action == 'delete' and pk:
        dish_instance.delete()
        return redirect('dish_list')

    # Preparação de dados para o formulário
    dish_types = DishType.objects.all()
    cooks = Cook.objects.all()

    context = {
        'dishes': Dish.objects.all(),
        'dish_types': dish_types,
        'cooks': cooks,
        'editing_dish': dish_instance if pk and action == 'edit' else None
    }
    return render(request, 'restaurant/manage_dishes.html', context)
