from django.contrib import admin
from main .models import Product_Database

# Register your models here.
class AccountA(admin.ModelAdmin):
    model=Product_Database
    list_display=['id','name','email','product_name','price','link']
admin.site.register(Product_Database,AccountA)
