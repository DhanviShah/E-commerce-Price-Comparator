from smtplib import SMTP
import requests
import time
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}

flipkart_string = ''
amazon_string = ''
olx_string = ''

def convert(a):
    b=a.replace(" ",'')
    c=b.replace("INR",'')
    d=c.replace(",",'')
    f=d.replace("₹",'')
    g=int(float(f))
    return g

#---------------FLIPKART----------------#
def flipkart(name) :
  try :
    global flipkart_string
    product_name = name.replace(" ","+")
    flipkart_string = f'https://www.flipkart.com/search?q={product_name}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
    res = requests.get(f'https://www.flipkart.com/search?q={product_name}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off',headers=headers)
    print("\nSearching in Flipkart...")
    soup = BeautifulSoup(res.text,'html.parser')
    flipkart_name = soup.select('._4rR01T')[0].getText().strip()
    flipkart_name = flipkart_name.upper()
    if name.upper() in flipkart_name :
      flipkart_price = soup.select('._1_WHN1')[0].getText().strip()
      flipkart_name = soup.select('._4rR01T')[0].getText().strip()
      print("Flipkart:")
      print("Description : ", flipkart_name)
      print("Price : ", flipkart_price)
      print("----------")
    else :
      print("Flipkart : Product Not Found")
      flipkart_price = '0'
    return flipkart_price
  except:
      print("Flipkart : No product found!")  
      print("-----------------------")
      flipkart_price= '0'
  return flipkart_price   

#---------------AMAZON----------------#
def amazon(name) :
  try :
    global amazon_string
    #product_name1 = name.replace(" ","-")
    product_name2 = name.replace(" ","+")
    amazon_string = f'https://www.amazon.in/s?k={product_name2}'
    res = requests.get(f'https://www.amazon.in/s?k={product_name2}',headers=headers)
    print("\nSearching in Amazon ...")
    soup = BeautifulSoup(res.text,'html.parser')
    #print(soup)
    amazon_page = soup.select('.a-color-base.a-text-normal')
    amazon_page_length = int(len(amazon_page))
    for i in range (0,amazon_page_length) :
      name = name.upper()
      amazon_name = soup.select('.a-color-base.a-text-normal')[i].getText().strip().upper()
      if name in amazon_name[0:20] :
        amazon_name = soup.select('.a-color-base.a-text-normal')[i].getText().strip().upper()
        amazon_price = soup.select('.a-price-whole')[i].getText().strip().upper()
        print("Amazon:")
        print("Description :", amazon_name)
        print("Price :", '₹'+amazon_price)
        print('----------')
        break

      else :
        i+=1
        i = int(i)
        if i==amazon_page_length :
          print("Amazon : No Product Found!")
          amazon_price = '0'
          break
    return amazon_price
  except:
        print("Amazon: No Product Found!")
        print("-----------------------")
        amazon_price = '0'
  return amazon_price

#---------------OLX----------------#
def olx(name) :
    try:
        global olx_string
        name1 = name.replace(" ","-")
        olx_string=f'https://www.olx.in/items/q-{name1}?isSearchCall=true'
        res = requests.get(f'https://www.olx.in/items/q-{name1}?isSearchCall=true',headers=headers)
        print("\nSearching in OLX...")
        soup = BeautifulSoup(res.text,'html.parser')
        olx_name = soup.select('._2tW1I')
        olx_page_length = len(olx_name)
        for i in range(0,olx_page_length):
            olx_name = soup.select('._2tW1I')[i].getText().strip()
            name = name.upper()
            olx_name = olx_name.upper()
            if name in olx_name:
                olx_price = soup.select('._89yzn')[i].getText().strip()
                olx_name = soup.select('._2tW1I')[i].getText().strip()
                #olx_loc = soup.select('.tjgMj')[i].getText().strip()
                #try:
                    #label = soup.select('._2Vp0i span')[i].getText().strip()
                #except:
                    #label = "OLD"
                
                print("Olx:")
                #print(label)
                print("Description :", olx_name)
                print("Price", olx_price)
                #print(olx_loc)
                print('\n')
                break
            else:
                i+=1
                i=int(i)
                if i==olx_page_length:
                    print("Olx: No product Found!")
                    print("-----------------------")
                    olx_price = '0'
                    break
        return olx_price
    except:
        print("Olx: No product Found!")
        print("-----------------------")
        olx_price = '0'
    return olx_price

#-------------MAIN-------------#
name = input("\nEnter the product you want to search:")
flipkart_price = flipkart(name)
amazon_price = amazon(name)
olx_price = olx(name)
print("----------")

if flipkart_price=='0':
    print("No product found!")
    flipkart_price = int(flipkart_price)
else:
    print("FLipkart Price:",flipkart_price)
    flipkart_price=convert(flipkart_price)

if amazon_price=='0':
    print("No Product found!")
    amazon_price = int(amazon_price)
else:
    print("Amazon price: ₹",amazon_price)
    amazon_price=convert(amazon_price)

if olx_price =='0':
    print("No product found!")
    olx_price = int(olx_price)
else:
    print("Olx Price:",olx_price)
    olx_price=convert(olx_price)

time.sleep(2)
lst = [flipkart_price,amazon_price,olx_price]
lst2 = []
for j in range (0,len(lst)) :
  if lst[j]>0 :
    lst2.append(lst[j])

if len(lst2)==0 :
    print("No such relative product found in all the websites!")
else :
    min_price = min(lst2)
min_price = min(lst2)

print("_____________________")
print("\nMinimum Price : ₹",min_price)
