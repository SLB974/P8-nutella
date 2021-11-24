# coding: utf-8
""" Module for :
                    Fetching openfoodfacts data
                    cleaning data
                    save data in database
                    """

import json

import requests

from .models import Category, Product
from .utils import categories, criterias


class ApiConsulter:
    """Manage API's requests, data cleaning and saving."""

    @classmethod
    def get_results(cls, category):
        """API's GET consultation.

        parameter : category = searching category

        return : string
        """
        
        url = "https://fr.openfoodfacts.org/cgi/search.pl?"

        criterias['tag_1'] = category

        response = requests.get(url, params=criterias)
        response = response.json()

        return response
    
    @classmethod
    def db_clean(cls):
        """ clean existing records in database """
        Category.objects.all().delete()
        Product.objects.all().delete()
        
    @classmethod
    def db_save(cls):
        """ write data in db """
        
        expected = len(categories)
        actual = Category.objects.count()
        print(expected, actual)
        
        if expected != actual :
        
            cls.db_clean()
            
            for category in categories:
                data = Category.objects.create(category=category)
                data.save()
                last = Category.objects.last()
                
                response = cls.get_results(category)
                
                records = []
                
                for record in response["products"]:
                    
                    if 'nutrition_grade_fr' in record:
                    
                        data = Product(product=record['product_name'],
                                    category_id = last,
                                    brand=record['brands'],
                                    score=record['nutrition_grade_fr'])
                        
                        records.append(data)
                
                Product.objects.bulk_create(records)
