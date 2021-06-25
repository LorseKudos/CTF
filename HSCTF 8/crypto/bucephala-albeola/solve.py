import string
from pwn import *

r = remote('bucephala-albeola.hsc.tf', 1337)

r.recvuntil("key: ")

r.sendline(b"a")
enc = r.recvline().decode('utf-8').strip().split()[1:]
enc = list(map(int, enc))

print(enc)

rule = dict()

for c in string.ascii_lowercase:
    print(c)
    r.recvuntil(": ")

    r.sendline(c.encode())
    rule[c] = int(r.recvline().split()[1])

min_num = min(rule.values())

for i in rule.keys():
    rule[i] -= min_num - 11

for i in range(len(enc)):
    enc[i] -= rule['a']

print(min_num)
print(rule)

rule_swap = {v: k for k, v in rule.items()}

print(enc)

for i in enc:
    print(rule_swap[i], end="")
