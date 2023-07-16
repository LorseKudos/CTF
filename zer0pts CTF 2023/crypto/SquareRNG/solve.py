#!/usr/bin/env python3
from pwn import *

r = remote('crypto.2023.zer0pts.com', 10666)

r.recvuntil(b"Bob's seed 1: ")
r.sendline(b"1")
r.recvuntil(b"Bob's seed 2: ")
r.sendline(b"-1")


for _ in range(77):
    rand1 = int(r.recvline().split()[-1].decode(), 0) >> 31
    rand2 = int(r.recvline().split()[-1].decode(), 0) % 2
    print(rand1, rand2)

    r.recvuntil(b"Guess next bool [0 or 1]: ")
    if rand1 ^ rand2 == 0:
        r.sendline(b"1")
    else:
        r.sendline(b"0")
    r.recvline()

r.interactive()

# zer0pts{L(a)L(b)=L(ab)}
