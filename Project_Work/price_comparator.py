from smtplib import SMTP
import requests
import time
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}

flipkart_string = ''
olx_string = ''

def convert(a):
    b=a.replace(" ",'')
    c=b.replace("INR",'')
    d=c.replace(",",'')
    f=d.replace("₹",'')
    g=int(float(f))
    return g

def flipkart(name) :
  try :
    global flipkart_string
    product_name = name.replace(" ","+")
    flipkart_string = f'https://www.flipkart.com/search?q={product_name}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
    res = requests.get(f'https://www.flipkart.com/search?q={product_name}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off',headers=headers)
    print("\nSearching in flipkart...")
    soup = BeautifulSoup(res.text,'html.parser')
    flipkart_name = soup.select('._4rR01T')[0].getText().strip()
    flipkart_name = flipkart_name.upper()
    if name.upper() in flipkart_name :
      flipkart_price = soup.select('._1_WHN1')[0].getText().strip()
      flipkart_name = soup.select('._4rR01T')[0].getText().strip()
      print("Flipkart:")
      print(flipkart_name)
      print(flipkart_price)
      print("----------")
    else :
      print("Flipkart : Product Not Found")
      flipkart_price = '0'
    return flipkart_price
  except:
      print("Flipkart:No product found!")  
      print("-----------------------")
      flipkart_price= '0'
  return flipkart_price    

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
                olx_loc = soup.select('.tjgMj')[i].getText().strip()
                try:
                    label = soup.select('._2Vp0i span')[i].getText().strip()
                except:
                    label = "OLD"
                
                print("Olx:")
                print(label)
                print(olx_name)
                print(olx_price)
                print(olx_loc)
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
        print("Olx: No product found!")
        print("-----------------------")
        olx_price = '0'
    return olx_price


name = input("\nEnter the product you want to search:")
flipkart_price = flipkart(name)
olx_price = olx(name)
print("----------")

if flipkart_price=='0':
    print("No product found!")
    flipkart_price = int(flipkart_price)
else:
    print("\nFLipkart Price:",flipkart_price)
    flipkart_price=convert(flipkart_price)

if olx_price =='0':
    print("No product found!")
    olx_price = int(olx_price)
else:
    print("\nOlx Price:",olx_price)
    olx_price=convert(olx_price)

time.sleep(2)
lst = [flipkart_price,olx_price]
lst2 = []
for j in range (0,len(lst)) :
  if lst[j]>0 :
    lst2.append(lst[j])
min_price = min(lst2)

print("----------")
print("\nMinimum Price : ₹",min_price)
