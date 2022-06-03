import requests

url = 'https://crumbs.web.actf.co/'
endpoint = ''

while 1:
    response = requests.get(url + endpoint)
    print(response.text)

    endpoint = response.text.split()[2]
