from Crypto.Util.number import bytes_to_long, long_to_bytes
import random
import math

print(bytes_to_long(b"fl"))

n = 30967
e1 = 5
d1 = 24493
e2 = 7
ct = 28355
p, q = 179, 173

phi = (p-1) * (q-1)
d2 = pow(e2, -1, phi)

print(e1*d1)
print(f"{phi = }")
print(f"{d2 = }")

print(long_to_bytes(pow(ct, d2, n)))
