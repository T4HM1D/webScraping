import requests
from bs4 import BeautifulSoup
# url = "https://www.keychron.uk/collections/keychron-uk-iso-layout-keyboards"
url = "https://www.keychron.uk/collections/new-arrivals"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
priceFile = open('priceFile.txt', 'w')

itemsContent = soup.find_all('div', class_='grid-product__content')
itemPrice = soup.find_all('div', class_='grid-product__price')
ogPrice = itemPrice[1].find('span', class_='grid-product__price--original')
salePrice = itemPrice[1].find('span', class_='sale-price').text.strip()
# print(itemPrice[0].text.strip())
# print(salePrice)
# i = itemPrice[1]
# if i.find('span', class_='sale-price') != None:
#     print(i.find('span', class_='sale-price').text.strip())
# else:
#     print(i.text.strip())

for i in range(len(itemsContent)):
    itemName = itemsContent[i].find('div', class_='grid-product__title').text
    print(itemName)
    price = itemPrice[i]
    if price.find('span', class_='sale-price') != None:
        sale = price.find('span', class_='sale-price').text.strip()
        og = price.find('span', class_='grid-product__price--original').text
        saleString = "\n Sale price: %s, original price: %s \n" % (sale, og)
        print(saleString)
        priceFile.write(itemName)
        priceFile.write(saleString)

    else:
        normalPrice = price.text.strip()
        normalString = "\n Regular Price: %s \n" % (normalPrice)
        print(normalString)
        priceFile.write(itemName)
        priceFile.write(normalString)