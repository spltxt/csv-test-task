from django.db import models


class Product(models.Model):
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=500)
    level_one = models.CharField(max_length=100)
    level_two = models.CharField(max_length=100)
    level_three = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    alt_price = models.CharField(max_length=50)
    quantity = models.CharField(max_length=100)
    property_fields = models.CharField(max_length=100)
    joint_purchases = models.CharField(max_length=100)
    measure_unit = models.CharField(max_length=30)
    image = models.CharField(max_length=1000)
    display_on_index = models.CharField(max_length=100)
    description = models.TextField()
