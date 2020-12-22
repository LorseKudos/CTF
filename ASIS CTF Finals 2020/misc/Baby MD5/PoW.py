from hashlib import *
import random
import string
import re
from pwn import *

r = remote('66.172.10.203', 2570)

text = r.recvline().decode('utf-8')
print(text)
p = r'Please submit a printable string X, such that (.+)\(X\)\[-6:\] \= (.+) and len\(X\) \= (\d+).*'
m = re.match(p, text)
ans = m.group(2)
hash_func = m.group(1)
len_msg = int(m.group(3))

print(ans, hash_func, len_msg)

while True:
    text = ''.join([random.choice(string.printable[:-6]) for i in range(len_msg)])
    hash = locals()[hash_func](text.encode('utf-8')).hexdigest()[-6:]
    if hash == ans:
        break
print(text)
r.sendline(text)

r.interactive()

def babymd5(m, n, x_head, y_head, x, y):
    if x.startswith(x_head) and y.startswith(y_head):
        for _ in range(m):
            xhash = md5(x.encode('utf-8')).hexdigest()
            x = xhash
        for _ in range(n):
            yhash = md5(y.encode('utf-8')).hexdigest()
            y = yhash
        if xhash == yhash:
            return True
    return False


recv = r.recvuntil("[Q]uit\n")
print(recv)
r.sendline("C")

recv = r.recvline().decode('utf-8')
print(recv)
p = r".*\(m, n, x_head, y_head\) = \((\d+), (\d+), '(.+)', '(.+)'\).*"
m = re.match(p, text)
m, n, x_head, y_head = m.groups()
m, n = int(m), int(n)

print(m, n, x_head, y_head)


print(x_init, y_init)
r.interactive()
