from django.contrib import admin

# Register your models here.
from .models import Ingredient, Product, Category

admin.site.register(Ingredient)
admin.site.register(Product)
admin.site.register(Category)
