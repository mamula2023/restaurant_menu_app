from rest_framework.generics import ListAPIView

from restaurant.models import Restaurant
from restaurant.serializers import RestaurantSerializer


# Create your views here.
class RestaurantListView(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
