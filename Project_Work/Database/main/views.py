from django.shortcuts import render,redirect
from .models import Product_Database
import requests
from django.http import HttpResponse
#import time
from bs4 import BeautifulSoup
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
#amazon = ''
flipkart = ''
#croma = ''
# Create your views here.
def home(request):
    name='samsung galaxy s10'
    global flipkart
    product_name = name.replace(" ","+")
    flipkart = f'https://www.flipkart.com/search?q={product_name}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
    res = requests.get(f'https://www.flipkart.com/search?q={product_name}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off',headers=headers)
    print("\n Searching in flipkart...")
    soup = BeautifulSoup(res.text,'html.parser')
    flipkart_name = soup.select('._4rR01T')[0].getText().strip()
    flipkart_name = flipkart_name.upper()
    if name.upper() in flipkart_name :
      flipkart_price = soup.select('._1_WHN1')[0].getText().strip()
      flipkart_name = soup.select('._4rR01T')[0].getText().strip()
      name='flipkart'
      model=flipkart_name
      price=flipkart_price
      y=Product_Database.objects.filter(name=name,product=model).exists()
      if y==False:
        x=Product_Database(name=name,product=model,price=price)
        x.save()
      #print("-----------------")
    else :
      print("Flipkart : Product Not Found")
      flipkart_price = '0'
    return HttpResponse("Adding Successful!")


