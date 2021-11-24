from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    """ Model representing category """

    category = models.CharField(max_length=200, help_text="Enter a category name")
    
    def __str__(self):
        return self.category
class Product(models.Model):
    """ Model representing product with nutrition score """

    product = models.CharField(max_length=200, null=False, blank=False)
    category_id = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="related category"
    )
    brand=models.CharField(max_length=100, null=False, blank=False)
    score=models.CharField(max_length=1, null=False, blank=False)    

    def __str__(self):
        return self.product
    
class Favorites(models.Model):
    """ Model representing user's favorites """

    user_id=models.ForeignKey(
        User,
        on_delete=models.CASCADE, null=False, blank=False)

    product_id = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="related product"
    )
      