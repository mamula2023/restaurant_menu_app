from rest_framework.generics import ListAPIView

from restaurant.models import Restaurant, Category
from restaurant.serializers import RestaurantSerializer, CategorySerializer


# Create your views here.
class RestaurantListView(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
