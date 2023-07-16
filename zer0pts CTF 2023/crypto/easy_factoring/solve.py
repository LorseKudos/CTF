from sympy.abc import x, y, t
from sympy.solvers.diophantine.diophantine import diop_quadratic
from Crypto.Util.number import isPrime
from pwn import *

r = remote("crypto.2023.zer0pts.com", 10333)
N = int(r.readline().decode().split()[-1])

factors = diop_quadratic(x**2 + y**2 - N, t)

for p, q in factors:
    p, q = int(p), int(q)
    if isPrime(p) and isPrime(q):
        r.sendline(str(p).encode())
        r.sendline(str(q).encode())
        break

r.interactive()

# zer0pts{piyopiyo_Fermat's_Sum_of_Square_meow!!}
