from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # --- DishType CRUD & Detail ---
    path('dishtype/manage/', views.manage_dish_types, name='manage_dish_types'),
    path('dishtype/manage/<int:pk>/<str:action>/', views.manage_dish_types, name='manage_dish_types_action'),
    path('dishtypes/<int:pk>/', views.dishtype_detail, name='dishtype_detail'),  # NOVO

    # --- Cook CRUD & Detail ---
    path('cooks/', views.cook_list, name='cook_list'),
    path('cooks/manage/', views.manage_cooks, name='manage_cooks'),
    path('cooks/manage/<int:pk>/<str:action>/', views.manage_cooks, name='manage_cooks_action'),
    path('cooks/<int:pk>/', views.cook_detail, name='cook_detail'),  # NOVO

    # --- Ingredient CRUD ---
    path('ingredients/', views.ingredient_list, name='ingredient_list'),
    path('ingredients/manage/', views.manage_ingredients, name='manage_ingredients'),
    path('ingredients/manage/<int:pk>/<str:action>/', views.manage_ingredients, name='manage_ingredients_action'),

    # --- Dish CRUD & Detail (Adicionando Detail) ---
    path('dishes/', views.dish_list, name='dish_list'),
    path('dishes/manage/', views.manage_dishes, name='manage_dishes'),
    path('dishes/manage/<int:pk>/<str:action>/', views.manage_dishes, name='manage_dishes_action'),
    path('dishes/<int:pk>/', views.dish_detail, name='dish_detail'),  # NOVO
]
