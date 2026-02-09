from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dishtype/list/', views.dish_type_list, name='dish_type_list'),
    path('dishtype/create/', views.dish_type_create, name='dish_type_create'),
    path('dishtype/update/<int:pk>/', views.dish_type_update, name='dish_type_update'),
    path('dishtype/delete/<int:pk>/', views.dish_type_delete, name='dish_type_delete'),
    path('cooks/', views.cook_list, name='cook_list'),
    path('cooks/create/', views.cook_create, name='cook_create'),
    path('cooks/update/<int:pk>/', views.cook_update, name='cook_update'),
    path('cooks/delete/<int:pk>/', views.cook_delete, name='cook_delete'),
    path('cooks/<int:pk>/', views.cook_detail, name='cook_detail'),
    path('ingredients/', views.ingredient_list, name='ingredient_list'),
    path('ingredients/create/', views.ingredient_create, name='ingredient_create'),
    path('ingredients/update/<int:pk>/', views.ingredient_update, name='ingredient_update'),
    path('ingredients/delete/<int:pk>/', views.ingredient_delete, name='ingredient_delete'),
    path('dishes/', views.dish_list, name='dish_list'),
    path('dishes/create/', views.dish_create, name='dish_create'),
    path('dishes/update/<int:pk>/', views.dish_update, name='dish_update'),
    path('dishes/delete/<int:pk>/', views.dish_delete, name='dish_delete'),
    path('dishes/<int:pk>/', views.dish_detail, name='dish_detail'),
]
