import requests
from bs4 import BeautifulSoup
url = "https://www.keychron.uk/collections/all-products"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
priceFile = open('priceFile.txt', 'w')

# itemsContent = soup.find_all('div', class_='grid-product__content')
# itemPrice = soup.find_all('div', class_='grid-product__price')
# for i in range(len(itemsContent)):
#     itemName = itemsContent[i].find('div', class_='grid-product__title').text
#     print(itemName)
#     price = itemPrice[i]
#     if price.find('span', class_='sale-price') != None:
#         sale = price.find('span', class_='sale-price').text.strip()
#         og = price.find('span', class_='grid-product__price--original').text
#         saleString = "\nSale price: %s, original price: %s\n" % (sale, og)
#         print(saleString)
#         priceFile.write(itemName)
#         priceFile.write(saleString)

#     else:
#         normalPrice = price.text.strip()
#         normalString = "\nRegular Price: %s\n" % (normalPrice)
#         print(normalString)
#         priceFile.write(itemName)
#         priceFile.write(normalString)


pages = soup.find('div', class_='pagination')
urls = []
links = pages.find_all('span', class_='page')
for i in range(len(links)):
    tags = links[i].find_all('a')
    for tag in tags:
        pageNum = int(tag.text) if tag.text.isdigit() else None
        if pageNum != None:
            split = tag.get('href').split('products')
            print(split)
            x = split[-1]
            urls.append(x)
print(urls)

for i in urls:
    newUrl = url + i
    response = requests.get(newUrl)
    soup = BeautifulSoup(response.text, 'lxml')

    itemsContent = soup.find_all('div', class_='grid-product__content')
    itemPrice = soup.find_all('div', class_='grid-product__price')

    for j in range(len(itemsContent)):
        itemName = itemsContent[j].find(
            'div', class_='grid-product__title').text
        print(itemName)
        price = itemPrice[j]
        if price.find('span', class_='sale-price') != None:
            sale = price.find('span', class_='sale-price').text.strip()
            og = price.find(
                'span', class_='grid-product__price--original').text
            saleString = "\nSale price: %s, original price: %s\n" % (sale, og)
            print(saleString)
            priceFile.write(itemName)
            priceFile.write(saleString)
        else:
            normalPrice = price.text.strip()
            normalString = "\nRegular Price: %s\n" % (normalPrice)
            print(normalString)
            priceFile.write(itemName)
            priceFile.write(normalString)
