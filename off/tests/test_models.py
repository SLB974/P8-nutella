""" testing off models """

from django.test import TestCase
from off.models import Category, Favorite, Product


class CategoryModelTest(TestCase):
    def setUp(self):
        pass
    
    def pk_should_be_one(self):
        pass

class ProductModelTest(TestCase):
    pass

class FavoriteModelTest(TestCase):
    pass

        
    