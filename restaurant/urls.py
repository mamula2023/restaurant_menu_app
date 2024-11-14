from django.urls import path, include
from rest_framework.routers import DefaultRouter

from restaurant.views import RestaurantListView, CategoryListView

router = DefaultRouter()

urlpatterns = [
    path('restaurants/', RestaurantListView.as_view(), name='restaurant-list'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
]
