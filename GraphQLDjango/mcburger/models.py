from django.db import models
from django.db.models import CASCADE


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Ingredient(models.Model):
    name = models.CharField(max_length=150, unique=True)
    extra_price = models.FloatField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, unique=True)
    price = models.FloatField()
    ingredients = models.ManyToManyField(Ingredient)
    category = models.ForeignKey(Category,
                                 related_name="products",
                                 on_delete=CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
