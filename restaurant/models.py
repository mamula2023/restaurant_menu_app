from django.db import models


# Create your models here.

class Restaurant(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True, default='images/default.jpg')
    categories = models.ManyToManyField('Category', related_name='restaurants')

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, default='images/default.jpg')

    def __str__(self):
        return self.title


class Dish(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True, default='images/default.jpg')
    price = models.FloatField()
    category = models.ForeignKey(SubCategory, related_name='dishes', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    title = models.CharField(max_length=100)
    dish = models.ManyToManyField(Dish, related_name='ingredients')

    def __str__(self):
        return self.title