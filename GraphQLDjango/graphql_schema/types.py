import graphene
from graphene_django.types import DjangoObjectType

from mcburger.models import Category, Product

import json


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class Query(object):
    products = graphene.List(ProductType)
    categories = graphene.List(CategoryType)

    def resolve_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_products(self, info, **kwargs):
        return Product.objects.select_related('category').all()
