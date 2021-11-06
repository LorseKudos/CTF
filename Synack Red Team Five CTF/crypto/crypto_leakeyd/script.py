from Crypto.Util.number import getPrime, bytes_to_long
from math import gcd

# flag = open("flag.txt").read().strip().encode()
flag = b"fl"

p = getPrime(8)
q = getPrime(8)
n = p * q
e1 = 0x5
e2 = 0x7


assert gcd(p-1,e1) == 1 and gcd(q-1, e1) == 1 and gcd(p-1,e2) == 1 and gcd(q-1, e2) == 1

phi = (p-1) * (q-1)
d1 = pow(e1, -1, phi)
print(f"""Retrieved agent data:
n = {n}
e = {e1}
d = {d1}""")

ct = pow(bytes_to_long(flag), e2, n)
print(f"""Spy messages:
e = {e2}
ct = {ct}""")

print(p, q)
