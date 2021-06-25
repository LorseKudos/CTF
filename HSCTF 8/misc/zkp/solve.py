from pwn import * # pip install pwntools

r = remote('zkp.hsc.tf', 1337)

r.recvline()
T=int(r.recvline().decode())
print("T: {}".format(T))
for t in range(T):
    print("t: {}".format(t))
    n=r.recvline().decode()
    print(n)
    n=int(n)
    m=r.recvline().decode()
    print(m)
    m=int(m)
    p=1.0
    ok=True
    while True:
        # print(r.recvline().decode())
        r.recvuntil(": ")
        r.sendline("1")
        s=r.recvline().decode()
        print(s)
        if s.count("False")==3:
            ok=False
            break
        if p<0.75:
            break
        r.sendline("next")
        p*=(m-1)/m
        # print(p)
    print(ok)
    if ok:
        r.sendline("true")
    else:
        r.sendline("false")
