#!/usr/bin/env python3
from pwn import *

def pad(data, bsize):
    b = bsize - len(data) % bsize
    return data + bytes([b] * b)

def xor(a, b):
    return bytes(aa ^ bb for aa, bb in zip(a, b))


r = remote('babymac.hackable.software', 1337)

r.recvuntil(b"> ")
r.sendline(b"sign")
r.recvuntil(b"> ")
r.sendline(b"")

enc = bytes.fromhex(r.recvline().decode())
mes = bytes.hex(pad(b"", 16) + b"\x00"*16 + xor(enc, pad(b"gimme flag", 16)))

r.recvuntil(b"> ")
r.sendline(b"sign")
r.recvuntil(b"> ")
r.sendline(mes.encode('utf-8'))

enc = bytes.fromhex(r.recvline().decode())[:16]
mes = bytes.hex(enc + pad(b"gimme flag", 16))

r.recvuntil(b"> ")
r.sendline(b"verify")
r.recvuntil(b"> ")
r.sendline(mes.encode('utf-8'))

print(r.recvline())
