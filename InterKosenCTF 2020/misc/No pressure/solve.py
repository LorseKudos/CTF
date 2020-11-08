from pwn import *

r = remote('misc.kosenctf.com', 10002)

flag = "KosenCTF{"
while True:
    for i in range(33, 126):
        r.sendline(flag + chr(i))
        enc = r.recvline()
        if len(enc) < 135:
            flag += chr(i)
            print(flag)
            break

    if flag[-1] == '}':
        break

print(flag)
