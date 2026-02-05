from django.urls import path
from . import views

app_name = 'restaurant'

urlpatterns = [
    path('criar_restaurant/', views.Criar_Restaurant, name='criar_restaurant'),
    # DishType Views
    path('types/', views.DishTypeList.as_view(), name='dishtype_list'),
    path('types/<int:pk>/', views.DishTypeDetail.as_view(), name='dishtype_detail'),

    # Dish Views
    path('dishes/', views.DishList.as_view(), name='dish_list'),
    path('dishes/<int:pk>/', views.DishDetail.as_view(), name='dish_detail'),

    # Cook Views
    path('cooks/', views.CookList.as_view(), name='cook_list'),
    path('cooks/<int:pk>/', views.CookDetail.as_view(), name='cook_detail'),
]
