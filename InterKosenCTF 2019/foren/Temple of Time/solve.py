from scapy.all import *
from scapy.layers import http
from urllib.parse import *
import re

packets = rdpcap("temple_of_time.pcapng")

for packet in packets:
    if packet.haslayer(http.HTTPRequest):
        http_layer = packet.getlayer(http.HTTPRequest).fields
        ip_layer = packet.getlayer('IP').fields
        if "SELECT" in http_layer['Path'].decode(encoding='utf-8'):
            request_time = packet.time
            request_url = unquote_plus(
                http_layer['Path'].decode(encoding='utf-8'))
    if packet.haslayer(http.HTTPResponse):
        http_layer = packet.getlayer(http.HTTPResponse).fields
        ip_layer = packet.getlayer('IP').fields
        if packet.wirelen == 683 and packet.time - request_time > 1:
            m = re.search(r"=([0-9]+),SLEEP\(1\),''\)\)\)#\Z", request_url)
            if m:
                print(chr(int(m.group(1))), end='')
