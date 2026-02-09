from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dishtype/list/', views.dish_type_list, name='dish_type_list'),
    path('dishtype/create/', views.dish_type_create, name='dish_type_create'),
    path('dishtype/update/<int:pk>/', views.dish_type_update, name='dish_type_update'),
    path('dishtype/delete/<int:pk>/', views.dish_type_delete, name='dish_type_delete'),
    path('cooks/', views.cook_list, name='cook_list'),
    path('cooks/manage/', views.manage_cooks, name='manage_cooks'),
    path('cooks/manage/<int:pk>/<str:action>/', views.manage_cooks, name='manage_cooks_action'),
    path('cooks/<int:pk>/', views.cook_detail, name='cook_detail'),
    path('ingredients/', views.ingredient_list, name='ingredient_list'),
    path('ingredients/manage/', views.manage_ingredients, name='manage_ingredients'),
    path('ingredients/manage/<int:pk>/<str:action>/', views.manage_ingredients, name='manage_ingredients_action'),
    path('dishes/', views.dish_list, name='dish_list'),
    path('dishes/manage/', views.manage_dishes, name='manage_dishes'),
    path('dishes/manage/<int:pk>/<str:action>/', views.manage_dishes, name='manage_dishes_action'),
    path('dishes/<int:pk>/', views.dish_detail, name='dish_detail'),
]
