from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import DishType, Dish, Cook



class DishTypeCreateView(CreateView):
    model = DishType
    fields = ['name']
    template_name = 'restaurant/dishtype_form.html'
    success_url = reverse_lazy('restaurant:dishtype_list')

    def get_success_url(self):
        return reverse_lazy('restaurant:dishtype_list')

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
