from scapy.all import *
from scapy.layers import http
from urllib.parse import *
import re
from bs4 import BeautifulSoup


def calc_ans(hints):
    for i in range(150):
        flag = True
        for mod, rem in hints:
            if i % mod != rem:
                flag = False
        if flag:
            return chr(i)


packets = rdpcap("packet.pcap")
prev = 1
attack = False
hints = []
ans = ""

payload = r"secret\, ([0-9]+)\, 1\)\) FROM account WHERE name\=\"admin\"\) \% ([0-9]+)"

for packet in packets:
    if packet.haslayer(http.HTTPRequest):
        http_layer = packet.getlayer(http.HTTPRequest).fields
        if "SELECT" in http_layer['Path'].decode(encoding='utf-8'):
            request_url = unquote_plus(
                http_layer['Path'].decode(encoding='utf-8'))

            m = re.search(payload, request_url)
            idx, mod = int(m.group(1)), int(m.group(2))
            if idx != prev:
                ans += calc_ans(hints)
                prev = idx
                hints = []
            attack = True
    if packet.haslayer(http.HTTPResponse) and attack:
        html = packet.getlayer(
            http.HTTPResponse).load
        tbl = BeautifulSoup(html, "html.parser").findAll(
            "table", {"class": "table-striped"})
        if tbl:
            hints.append([mod, len(tbl[0].findAll("tr"))-1])

print(ans)
