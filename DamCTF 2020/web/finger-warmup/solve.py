import requests
from bs4 import BeautifulSoup

url = 'https://finger-warmup.chals.damctf.xyz/'
endpoint = ''

while 1:
    response = requests.get(url + endpoint)

    soup = BeautifulSoup(response.text, "html.parser")
    print(soup)
    endpoint = soup.find('a').get('href')

