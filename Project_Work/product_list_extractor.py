from selenium import webdriver as wb
from bs4 import BeautifulSoup

def croma_product_list(search):
    product_name = search.replace(" ","+")
    croma_string = f'https://croma.com/search/?text={product_name}'
    driver.get(croma_string)
    #time.sleep(10)
    soup = BeautifulSoup(driver.page_source,'html.parser')
    results = soup.find_all('li',{'class':'product-item'})
    #time.sleep(20)
    print('total results: ', len(results))
    price_list = []
    url = []
    description_list = []
    image_url = []
    for item in results:
        try:
            image_object = item.find('img')
            image = image_object.get('src')
            image_url.append(image)
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
    for iterator in range(len(description_list)):
        try:
            print('Product - ',iterator+1)
            print('Description: ', description_list[iterator])
            print('price: \u20B9',price_list[iterator])
            print('Image Link: ',image_url[iterator])
            print('Redirection Link: ',url[iterator])
            print('\n')
        except:
            continue

def amazon_product_list(search):
    product_name = search.replace(" ","+")
    amazon_string = f'https://www.amazon.in/s?k={product_name}'
    driver.get(amazon_string)
    soup = BeautifulSoup(driver.page_source,'html.parser')
    results = soup.find_all('div',{'data-component-type':'s-search-result'})
    print('total results: ',len(results))
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

    for iterator in range(len(description_list)):
        try:
            print('Product - ',iterator+1)
            print('Description: ', description_list[iterator])
            print('price: \u20B9',price_list[iterator])
            print('Image Link: ',image_url[iterator])
            print('Redirection Link: ',url[iterator])
            print('\n')
        except:
            continue
    
search = input('Enter the product for which you want a list: ')
driver = wb.Chrome('C:/Users/srishti kalra/Downloads/chromedriver.exe')
croma_product_list(search)
amazon_product_list(search)