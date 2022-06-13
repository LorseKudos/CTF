from Crypto.Util.number import *
# from secret import flag
from functools import reduce
from operator import mul


flag = "ctf4b{hogefuga}ctf4b{hogefuga}ctf4b{hogefuga}ctf4b{hogefu"

bits = 256
flag = bytes_to_long(flag.encode())
print(flag.bit_length())
assert flag.bit_length() == 455
print(flag)
GUESTS = []


def invite(p):
    global GUESTS
    if isPrime(p):
        print("[*] We have been waiting for you!!! This way, please.")
        GUESTS.append(p)
    else:
        print("[*] I'm sorry... If you are not a Prime Number, you will not be allowed to join the party.")
    print("-*-*-*-*-*-*-*-*-*-*-*-*-")


invite(getPrime(bits))
invite(getPrime(bits))
invite(getPrime(bits))
invite(getPrime(bits))

for i in range(3):
    print("[*] Do you want to invite more guests?")
    num = int(input(" > "))
    invite(num)

print(GUESTS)
n = reduce(mul, GUESTS)
e = 65537
cipher = pow(flag, e, n)

print("n =", n)
print("e =", e)
print("cipher =", cipher)
