import requests
from bs4 import BeautifulSoup

data = []

for i in range(1, 8):
    fmt = 'https://scrapingclub.com/exercise/list_basic/?page={}'.format(i+1)
    response = requests.get(fmt)
    soup = BeautifulSoup(response.text, features="html.parser")
    a_fmt = soup.find_all('h4', class_='card-title')
    for i in range(len(a_fmt)):
        a_fmt[i] = a_fmt[i].find('a', href=True)['href']
    for i in range(len(a_fmt)):
        fmt = 'https://scrapingclub.com/{}'.format(a_fmt[i])
        response = requests.get(fmt)
        soup = BeautifulSoup(response.text, features="html.parser")
        name = soup.find('h3').text
        price = soup.find('div', class_='card-body').find('h4').text
        description = soup.find('p', class_='card-text').text
        data.append([name, price, description])

for i in range(len(data)):
    print(data)