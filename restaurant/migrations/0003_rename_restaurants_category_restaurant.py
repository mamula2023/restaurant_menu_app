# Generated by Django 5.1 on 2024-11-14 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_remove_category_restaurant_category_restaurants_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='restaurants',
            new_name='restaurant',
        ),
    ]
