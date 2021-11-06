from pwn import *


def xor(message, iv):
    return bytes([_a ^ _b for _a, _b in zip(message, iv)])


r = remote('aesnoc.crypto.wanictf.org', 50000)

flag = b"}"

iv = bytes.fromhex((r.recvline().decode().split()[2].strip("'")))

r.recvuntil(b"> ")
r.sendline(b"1")

enc_flag = bytes.fromhex((r.recvline().decode().split()[2].strip("'")))

following_flag = b"}"

for i in reversed(range(3)):
    r.recvuntil(b"> ")
    r.sendline(b"2")
    r.recvuntil(b"> ")
    r.sendline(following_flag.hex().encode())

    enc_xored = bytes.fromhex((r.recvline().decode().split()[2].strip("'")))
    enc = xor(enc_xored, iv)

    flag = xor(enc, enc_flag[16*(i+1):16*(i+2)]) + flag
    following_flag = flag[:16]

print(flag)
