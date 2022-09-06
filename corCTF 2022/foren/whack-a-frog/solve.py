from scapy.all import rdpcap
import os
import re

os.chdir(os.path.dirname(os.path.abspath(__file__)))
packets = rdpcap("whacking-the-froggers.pcap")

for packet in packets:
    if "anticheat" in str(packet):
        m = re.search(
            r"/anticheat\?x=(\d+)\&y=(\d+)\&event=(\w+)", str(packet))
        print(int(m.group(1)), int(m.group(2)), m.group(3))
