#!/usr/bin/env python3

from curses import KEY_A1
import random

with open("output.txt", "rb") as filp:
    xorrox, enc = 0, 0
    exec(filp.read())

key = [enc[0]^1]
flag = "f"

for i, v in enumerate(xorrox[1:], 1):
    k = 1^v
    for j in range(1, i):
        k ^= key[j]
    key.append(k)
    flag += chr(enc[i]^k)

print(flag)
