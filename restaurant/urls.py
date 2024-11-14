from django.urls import path, include
from rest_framework.routers import DefaultRouter

from restaurant.views import RestaurantListView

router = DefaultRouter()

urlpatterns = [
    path('restaurants/', RestaurantListView.as_view(), name='restaurant-list'),
]
