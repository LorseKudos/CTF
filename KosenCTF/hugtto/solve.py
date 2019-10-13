from PIL import Image
import re
import os
from datetime import datetime
import random

time = datetime(2019, 8, 6, 11, 44).strftime("%s")

base = os.path.dirname(os.path.abspath(__file__))
name = os.path.normpath(os.path.join(base, 'steg_emiru.png'))
img = Image.open(name)
new_img = Image.new("RGB", img.size)

w, h = img.size

length = 800

for t in range(60):
    bin_flag = []
    random.seed(int(time)+t)
    i = 0
    for x in range(w):
        for y in range(h):
            r, g, b = img.getpixel((x, y))
            rnd = random.randint(0, 2)
            if rnd == 0:
                r = (r & 0x01)
                bin_flag.append(str(r))
            elif rnd == 1:
                g = (g & 0x01)
                bin_flag.append(str(g))
            elif rnd == 2:
                b = (b & 0x01)
                bin_flag.append(str(b))
            i += 1
            if i == length:
                break
        if i == length:
            break

    result = ""
    for i in range(0, len(bin_flag), 8):
        result += chr(int("".join(list(reversed(bin_flag[i:i+8]))), 2))

    if re.match("KosenCTF", result):
        print(t)
        print(result)
