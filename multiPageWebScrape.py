import requests
from bs4 import BeautifulSoup

url = "https://www.keychron.uk/collections/all-products"
url2 = "https://www.keychron.uk/collections/keychron-uk-iso-layout-keyboards"
file = 'priceFile1.txt'
file2='priceFile2.txt'

def scrape(url,writeFileName):
	with open(writeFileName,'w') as file:
		url = url
		response = requests.get(url)
		soup = BeautifulSoup(response.text, 'lxml')

		if soup.find('div', class_='pagination') is not None:
			pages = soup.find('div', class_='pagination')
			urls = []
			links = pages.find_all('span', class_='page')
			for i in range(len(links)):
			    tags = links[i].find_all('a')
			    for tag in tags:
			        pageNum = int(tag.text) if tag.text.isdigit() else None
			        if pageNum != None:
			            split = tag.get('href').split('products')
			            x = split[-1]
			            urls.append(x)			
			count = 1
			for i in urls:
			    newUrl = url + i
			    response = requests.get(newUrl)
			    soup = BeautifulSoup(response.text, 'lxml')
			    itemsContent = soup.find_all('div', class_='grid-product__content')
			    itemPrice = soup.find_all('div', class_='grid-product__price')
			    for j in range(len(itemsContent)):
			        if (itemsContent[j].find('div', class_='grid-product__tag grid-product__tag--sold-out') is None):
			            itemName = itemsContent[j].find('div',class_='grid-product__title').text
			            price = itemPrice[j]
			            if price.find('span', class_='sale-price') != None:
			                sale = price.find('span', class_='sale-price').text.strip()
			                og = price.find('span',class_='grid-product__price--original').text
			                saleString = f"{str(count).zfill(2)} | Sale price: {sale} | Original price: {og} | {itemName}\n"
			                print(saleString)
			                file.write(saleString)
			            else:
			                normalPrice = price.text.strip()
			                normalString = f"{str(count).zfill(2)} | Regular Price: {normalPrice} | {itemName}\n"
			                print(normalString)
			                file.write(normalString)
			            count += 1
		else:
				itemsContent = soup.find_all('div', class_='grid-product__content')
				itemPrice = soup.find_all('div', class_='grid-product__price')
				count =1
				for j in range(len(itemsContent)):
						if (itemsContent[j].find('div', class_='grid-product__tag grid-product__tag--sold-out') is None):
								itemName = itemsContent[j].find('div',class_='grid-product__title').text
								price = itemPrice[j]
								if price.find('span', class_='sale-price') != None:
										sale = price.find('span', class_='sale-price').text.strip()
										og = price.find('span',class_='grid-product__price--original').text
										saleString = f"{str(count).zfill(2)} | Sale price: {sale} | Original price: {og} | {itemName}\n"
										print(saleString)
										file.write(saleString)
								else:
										normalPrice = price.text.strip()
										normalString = f"{str(count).zfill(2)} | Regular Price: {normalPrice} | {itemName}\n"
										print(normalString)
										file.write(normalString)
								count+=1

scrape(url,file)
scrape(url2,file2)
