from django.urls import path, include
from rest_framework.routers import DefaultRouter

from restaurant.views import RestaurantViewSet, CategoryViewSet, SubCategoryViewSet, SubCategoryDetailedListView

router = DefaultRouter()
router.register('restaurants', RestaurantViewSet)
router.register('categories', CategoryViewSet)
router.register('subcategories', SubCategoryViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
