from django.db import models

# Create your models here.
class Product_Database(models.Model):
    name=models.CharField(max_length=70)
    product=models.CharField(max_length=70)
    price=models.CharField(max_length=70)
