from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view, action
from rest_framework.generics import ListAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from socks import method

from restaurant.models import Restaurant, Category, SubCategory, Dish
from restaurant.serializers import RestaurantSerializer, CategorySerializer, SubCategorySerializer, DishSerializer


# Create your views here.

class RestaurantViewSet(
        mixins.ListModelMixin,
        GenericViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class CategoryViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    http_method_names = ['get', 'post', 'patch', 'post']
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryViewSet(mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         mixins.ListModelMixin,
                         GenericViewSet):
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()
    filter_fields = ['parent_id', 'dish_id']
    http_method_names = ['get', 'post', 'patch', 'post']

    #
    # def get_queryset(self):
    #     queryset = SubCategory.objects.all()
    #     parent_id = self.request.query_params.get('parent_id', None)
    #     dish_id = self.request.query_params.get('dish_id', None)
    #
    #     if parent_id is not None:
    #         queryset = queryset.filter(parent_id=parent_id)
    #
    #     if dish_id is not None:
    #         queryset = queryset.filter(dish_id=dish_id)
    #     return queryset


class SubCategoryDetailedListView(ListAPIView):
    serializer_class = DishSerializer

    def get_queryset(self):
        queryset = Dish.objects.all()
        subcategory_id = self.request.query_params.get('subcategory_id', None)
        title = self.request.query_params.get('title', None)

        if subcategory_id is not None:
            queryset = queryset.filter(category=subcategory_id)

        if title is not None:
            queryset = queryset.filter(title__icontains=title)

        return queryset
