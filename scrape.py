import requests
from bs4 import BeautifulSoup
url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

# checks every span tag with class "text" and stores it in a list.
qoutes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')


# for every quote in qoutes list
for i in range(len(qoutes)):
    print(qoutes[i].text)
    print(authors[i].text)
    quoteTags = tags[i].find_all('a', class_='tag')
    for tag in quoteTags:
        print(tag.text)
