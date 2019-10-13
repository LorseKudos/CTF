import os
from bs4 import BeautifulSoup
from socket import *

cookies = dict(session='18b2cbc4-ba88-41d5-a778-10d3329c369d',
               PHPSESSID='a0icn5jcr08b6dj8vdjo4nbp9t')


def get_dict():
    base = os.path.dirname(os.path.abspath(__file__))
    name = os.path.normpath(os.path.join(base, 'Kancolle Engine.html'))
    with open(name, encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, "html.parser")
    table = soup.findAll("table")[0]
    rows = table.findAll("tr")

    name_md5 = {}
    for row in rows[1:]:
        name_md5[row.findAll("td")[4].contents[0]] = row.findAll("td")[1].contents[0]
    return name_md5


name_md5 = get_dict()

s = socket(AF_INET, SOCK_STREAM)
s.connect(("maidakectf2019.aokakes.work", 12345))

count = 0
t = b''
while len(t) == 0 or t[-1] != ord(b'\n'):
    t += s.recv(1)

while count < 50:
    t = b''
    while len(t) == 0 or t[-1] != ord(b'\n'):
        t += s.recv(1)

    md5 = b''
    while len(md5) == 0 or md5[-1] != ord(b'\n'):
        md5 += s.recv(1)
    print(md5)

    t = s.recv(2)
    print(t)

    name = name_md5[md5.decode(encoding='utf-8')[:-1]]
    s.send(str(name).encode() + b'\n')

    count += 1
    print(count)

print(s.recv(255))
