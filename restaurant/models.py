from django.db import models


# Create your models here.

class Restaurant(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class Dish(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    price = models.FloatField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    title = models.CharField(max_length=100)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)

    def __str__(self):
        return self.title