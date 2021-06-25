from hashlib import *
import random
import string
import re
from pwn import *


def valid(str1):
    v = list("ABCDEFGHIKLMNPQRSTVWYZ")
    for i in str1:
        if i not in v:
            return False
    return True


def calc_evil_iv(iv, query):
    wrong_idx = re.search(r"[JOUX]", query).start()
    query = query.encode()

    iv = iv[:wrong_idx] + \
        (iv[wrong_idx] ^ query[wrong_idx] ^ ord("A")).to_bytes(1, byteorder="big") + iv[wrong_idx + 1:]

    return iv

if __name__ == "__main__":
    r = remote('canis-lupus-familiaris-bernardus.hsc.tf', 1337)

    r.recvuntil("V\n\n")
    for _ in range(100):
        query = r.recvuntil("? ").decode("utf-8").split()[1]

        if valid(query):
            r.sendline(b"T")
        else:
            r.sendline(b"F")
            r.recvline()
            iv = bytes.fromhex(r.recvuntil("use: ").decode("utf-8").split()[3])
            evil_iv = calc_evil_iv(iv, query)
            r.sendline(evil_iv.hex())
        print(r.recvline())

    r.interactive()
