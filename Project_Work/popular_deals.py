from selenium import webdriver as wb
from bs4 import BeautifulSoup

def amazon_product_list(search):
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
    i=0
    for item in results:
        try:
            image_object = item.find('img')
            image = image_object.get('src')
            image_url.append(image)
            atag = item.h2.a
            description = atag.text.strip()
            s = description.split("(",1)
            s = s[0]
            description_list.append(s)
            redirection_URL = 'https://www.amazon.in' + atag.get('href')
            url.append(redirection_URL)
            price_parent_class = item.find('span','a-price')
            amazon_price = price_parent_class.find('span','a-offscreen').text
            price = int(''.join(filter(lambda i: i.isdigit(), amazon_price)))
            price_list.append(price)
            i=i+1
            if i>3:
                break
        except:
            continue
    return description_list, price_list, image_url, url
    
search = ['mobile deals','ac deals','washing machine deals','refrigerator deals']
driver = wb.Chrome('C:/Users/srishti kalra/Downloads/chromedriver.exe')
des = []
price = []
img_url = []
redir_url = []
temp1 = []
temp2 = []
temp3 = []
temp4 = []
for i in range(len(search)):
    temp1,temp2,temp3,temp4 = amazon_product_list(search[i])
    des.extend(temp1)
    price.extend(temp2)
    img_url.extend(temp3)
    redir_url.extend(temp4)

driver.quit()

for iterator in range(len(des)):
    try:
        print('Product - ',iterator+1)
        print('Description: ', des[iterator])
        print('price: \u20B9',price[iterator])
        print('Image Link: ',img_url[iterator])
        print('Redirection Link: ',redir_url[iterator])
        print('\n')
    except:
        continue