from django.shortcuts import render,redirect
from .models import Product_Database
import requests
from .forms import UserSignUpForm,Search
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login as l,logout as g
from django.contrib import messages
from django.http import HttpResponse
from selenium import webdriver as wb
from bs4 import BeautifulSoup

def home(request):
  if request.method=='POST':
    fm=Search(request.POST)
    if fm.is_valid():
      name=fm.cleaned_data['name']
      return redirect('product',name)
  else:
    fm=Search()
  return render(request,'main/home.html', {'form':fm})

def login(request):
  if request.user.is_authenticated:
    return redirect('home')
  else:
    if request.method=='POST':
      fm=AuthenticationForm(request=request, data=request.POST)
      if fm.is_valid():
        username=fm.cleaned_data['username']
        password=fm.cleaned_data['password']
        user=authenticate(username=username,password=password)
        if user is not None:
          l(request,user)
          messages.success(request,'Login successfully')
          return redirect('home')
    else:
      fm=AuthenticationForm()
    return render(request,'main/login.html', { 'form': fm })

def signup(request):
  if request.user.is_authenticated:
    return redirect('home')
  else:
    if request.method=='POST':
      fm=UserSignUpForm(request.POST)
      if fm.is_valid():
        fm.save()
        return redirect('home')
    else:
      fm=UserSignUpForm()
    return render(request,'main/signup.html', { 'form': fm })

def logout(request):
    g(request)
    return redirect('home')

def product(request,product):
  form={}
  def amazon(search):
      #print('-----------searching in amazon-----------')
      product_name = search.replace(" ","+")
      amazon_string = f'https://www.amazon.in/s?k={product_name}'
      driver.get(amazon_string)
      soup = BeautifulSoup(driver.page_source,'html.parser')
      results = soup.find_all('div',{'data-component-type':'s-search-result'})
      #print('total results: ',len(results))
      price_list = []
      url = []
      description_list = []
      image_url = []
      for item in results:
          try:
              image_object = item.find('img')
              image = image_object.get('src')
              image_url.append(image)
              atag = item.h2.a
              description = atag.text.strip()
              description_list.append(description)
              redirection_URL = 'https://www.amazon.in' + atag.get('href')
              url.append(redirection_URL)
              price_parent_class = item.find('span','a-price')
              amazon_price = price_parent_class.find('span','a-offscreen').text
              price = int(''.join(filter(lambda i: i.isdigit(), amazon_price)))
              price_list.append(price)
          except:
              continue
      min_price = min(price_list)
      print('Description: ',description_list[price_list.index(min_price)])
      print('Price on amazon: \u20B9',min_price)
      print('Link:', url[price_list.index(min_price)])
      print('Imaga URL: ',image_url[price_list.index(min_price)] )    
          

  def croma(search):
      #print('-----------searching in croma-----------')
      product_name = search.replace(" ","+")
      croma_string = f'https://croma.com/search/?text={product_name}'
      driver.get(croma_string)
      #time.sleep(10)
      soup = BeautifulSoup(driver.page_source,'html.parser')
      results = soup.find_all('li',{'class':'product-item'})
      #time.sleep(20)
      #print('total results: ', len(results))
      price_list = []
      url = []
      description_list = []
      #image_url = []
      for item in results:
          try:
              '''image_object = item.find('img')
              image = image_object.get('src')
              image_url.append(image)'''
              atag = item.h3.a
              description = atag.text.strip()
              description_list.append(description)
              redirection_URL = 'https://www.croma.com' + atag.get('href')
              url.append(redirection_URL)
              croma_price = item.find('span',{'data-testid':'price'}).text
              price = (int(''.join(filter(lambda i: i.isdigit(), croma_price))))/100
              price_list.append(price)
          except:
              continue
      min_price = min(price_list)
      #print('Description: ',description_list[price_list.index(min_price)])
      #print('Link: ', url[price_list.index(min_price)])
      #print('Price on croma: \u20B9', min_price)
      #print('Imaga URL: ',image_url[price_list.index(min_price)] )


  def flipkart(search):
      #print('-----------searching in flipkart-----------')
      product_name = search.replace(" ","+")
      flipkart_string = f'https://www.flipkart.com/search?q={product_name}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
      driver.get(flipkart_string)
      soup = BeautifulSoup(driver.page_source,'html.parser')
      results = soup.find_all('div',{'class':'_1AtVbE col-12-12'})
      #print('total results: ',len(results))
      price_list = []
      url = []
      description_list = []
      for item in results:
          try:
              atag = item.a
              div_des = atag.find('div',{'class':'_4rR01T'})
              description = div_des.text.strip()
              description_list.append(description)
              redirection_URL = 'https://www.flipkart.com'+ atag.get('href')
              url.append(redirection_URL)
              flipkart_price = atag.find('div',{'class':'_30jeq3 _1_WHN1'}).text
              price = int(''.join(filter(lambda i: i.isdigit(), flipkart_price)))
              price_list.append(price)
          except:
              continue
      min_price = min(price_list)
      #print('Description: ',description_list[price_list.index(min_price)])
      #print('Price on flipkart: \u20B9',min_price)
      #print('Link:', url[price_list.index(min_price)])

  driver = wb.Chrome('F:/chromedriver/chromedriver.exe')
  amazon(product)
  croma(product)
  flipkart(product)
  if request.method=='POST':
    if request.user.is_authenticated==False:
      messages.info(request,'please login first, nakar halti no tha')
    else:
      pass
  return render(request,'main/product.html')