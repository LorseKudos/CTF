from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(("maidakectf2019.aokakes.work", 17270))

count = 0
t = b''
while len(t) == 0 or t[-1] != ord(b'\n'):
    t += s.recv(1)
t = b''
while len(t) == 0 or t[-1] != ord(b'\n'):
    t += s.recv(1)

while count < 500:
    t = b''
    while len(t) == 0 or t[-1] != ord(b'\n'):
        t += s.recv(1)

    expr = b''
    while len(expr) == 0 or expr[-1] != ord(b'\n'):
        expr += s.recv(1)
    print(expr)

    t = s.recv(2)
    print(t)

    ans = int(eval(expr))
    s.send(str(ans).encode() + b'\n')

    count += 1

print(s.recv(255))
