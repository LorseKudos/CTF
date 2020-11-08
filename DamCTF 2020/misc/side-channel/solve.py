from pwn import *
import time

r = remote('chals.damctf.xyz', 30318)

r.recvuntil('password[0] = ?\n')

password = ['']*8

for i in range(8):
    t1 = time.time()
    r.sendline('')
    enc = r.recvline()
    print(enc)
    t2 = time.time()
    elapsed_time = t2-t1
    print(elapsed_time*10)
    password[i] = format(int(elapsed_time*10)-1, 'x')

print(password)

for i in range(8):
    r.sendline(password[i])
    enc = r.recvline()
    print(enc)

enc = r.recvline()
print(enc)
# print(flag)
