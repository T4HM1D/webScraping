import requests
from bs4 import BeautifulSoup
# url = "https://www.keychron.uk/collections/keychron-uk-iso-layout-keyboards"
url = "https://www.keychron.uk/collections/new-arrivals"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

# items = soup.find_all('div', class_='grid__item grid-product small--one-half medium-up--one-quarter grid-product__has-quick-shop aos-init aos-animate')
itemsContent = soup.find_all('div', class_='grid-product__content')
itemPrice = soup.find_all('div', class_='grid-product__price')
ogPrice = itemPrice[1].find('span', class_='grid-product__price--original')
salePrice = itemPrice[1].find('span', class_='sale-price').text.strip()
print(itemPrice[0].text.strip())
# print(salePrice)

# for price in ogPrice:
#     print(price.text)


for i in range(len(itemsContent)):
    itemName = itemsContent[i].find('div', class_='grid-product__title').text
    print(itemName)
    itemPrice = itemsContent[i].find_all('div', class_='grid-product__price')
    for price in itemPrice:
        print(price.find('div', class_='sale-price'))
