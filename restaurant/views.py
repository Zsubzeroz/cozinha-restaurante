from django.views.generic import ListView, DetailView
from .models import Dish, DishType, Cook


class DishTypeList(ListView):
    model = DishType
    template_name = 'restaurant/dishtype_list.html'
    context_object_name = 'dish_types'


class DishTypeDetail(DetailView):
    model = DishType
    template_name = 'restaurant/dishtype_detail.html'
    context_object_name = 'dishtype'


class DishList(ListView):
    model = Dish
    template_name = 'restaurant/dish_list.html'
    context_object_name = 'dishes'


class DishDetail(DetailView):
    model = Dish
    template_name = 'restaurant/dish_detail.html'
    context_object_name = 'dish'


class CookList(ListView):
    model = Cook
    template_name = 'restaurant/cook_list.html'
    context_object_name = 'cooks'


class CookDetail(DetailView):
    model = Cook
    template_name = 'restaurant/cook_detail.html'
    context_object_name = 'cook'

