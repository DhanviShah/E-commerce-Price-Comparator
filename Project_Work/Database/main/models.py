from django.db import models

# Create your models here.
class Product_Database(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=70)
    product_name=models.CharField(max_length=70)
    price=models.IntegerField()
    link=models.CharField(max_length=70)

class dummy(models.Model):
    des=models.CharField(max_length=70)
    imag_url=models.CharField(max_length=512)
    linkA=models.CharField(max_length=1070)
    linkF=models.CharField(max_length=1070)
    linkC=models.CharField(max_length=1070)
    amazonP=models.IntegerField()
    flipkartP=models.IntegerField()
    cromaP=models.IntegerField()