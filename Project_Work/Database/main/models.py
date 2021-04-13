from django.db import models

# Create your models here.
class Product_Database(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=70)
    product_name=models.CharField(max_length=70)
    price=models.CharField(max_length=70)
