#!/usr/local/bin/python3

import string
import re
from pwn import *
from itertools import product


alpha = string.ascii_lowercase

def encrypt(msg, key):
    ret = ""
    i = 0
    for c in msg:
        if c in alpha:
            ret += alpha[(alpha.index(key[i]) + alpha.index(c)) % len(alpha)]
            i = (i + 1) % len(key)
        else:
            ret += c
    return ret

def decrypt(msg, key):
    ret = ""
    i = 0
    for c in msg:
        if c in alpha:
            ret += alpha[(alpha.index(c) - alpha.index(key[i])) % len(alpha)]
            i = (i + 1) % len(key)
        else:
            ret += c
    return ret


assert decrypt(encrypt("actf{aeagae_afafagage_}fleg", "hoge"), "hoge") == "actf{aeagae_afafagage_}fleg"


enc_keys = {}
enc_actf_set = set()
for key in product(alpha, repeat=4):
    key = "".join(key)
    enc_keys[encrypt("actf{", key)] = key
    enc_actf_set.add(encrypt("actf{", key))

print("finish")

context.log_level = 'debug'
r = remote('challs.actf.co', 31333)

r.recvline()

for i in range(100):
    print(i)
    enc = str(r.recvline().split()[2])
    print(enc)
    r.recvuntil("> ")

    for m in re.findall(r'[a-z]{4}\{\w+\}[a-z]{4}', enc):
        if m[:5] in enc_actf_set:
            key = enc_keys[m[:5]]
            mes = decrypt(m, key)
            if mes.endswith("}fleg"):
                print(mes)
                r.sendline(mes[:-4])
                break

r.interactive()
