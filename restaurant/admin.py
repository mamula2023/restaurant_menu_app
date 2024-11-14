from django.contrib import admin

from restaurant.models import Restaurant, Category, SubCategory, Dish

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Dish)
