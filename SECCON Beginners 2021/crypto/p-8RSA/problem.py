from Crypto.Util.number import *
from random import getrandbits
from os import urandom
# from flag import flag


flag = "c"

def gen_primes(bits, e):
    q = getPrime(bits)
    p = q
    while True:
        p = p-8 # p-8
        phi = (p - 1) * (q - 1)
        if isPrime(p) and GCD(phi, e) != 1:
            break
    return p, q


# flag = flag.encode("utf-8") + urandom(64)
flag = flag.encode("utf-8")
flag = bytes_to_long(flag)

e = 17
p, q = gen_primes(8, e)
n = p * q

print("flag =", flag)
print("p =", p)
print("q =", q)
print("n =", n)
print("e =", e)
print("c =", pow(flag, e, n))
