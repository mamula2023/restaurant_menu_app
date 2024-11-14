from rest_framework import serializers
from restaurant.models import Restaurant, Category, SubCategory, Dish, Ingredient


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'title']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['title', 'image']


class IngredientSerializer:
    class Meta:
        model = Ingredient
        fields = ['title']


class DishSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer()

    class Meta:
        model = Dish
        fields = ['title', 'image', 'ingredients']