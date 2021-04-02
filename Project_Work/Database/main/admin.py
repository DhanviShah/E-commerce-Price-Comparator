from django.contrib import admin
from main .models import Product_Database

# Register your models here.
class AccountA(admin.ModelAdmin):
    model=Product_Database
    list_display=['id','name','product','price']
admin.site.register(Product_Database,AccountA)
