from pwn import *
import random
import re


def untemper(x):
    x = unBitshiftRightXor(x, 18)
    x = unBitshiftLeftXor(x, 15, 0xefc60000)
    x = unBitshiftLeftXor(x, 7, 0x9d2c5680)
    x = unBitshiftRightXor(x, 11)
    return x


def unBitshiftRightXor(x, shift):
    i = 1
    y = x
    while i * shift < 32:
        z = y >> shift
        y = x ^ z
        i += 1
    return y


def unBitshiftLeftXor(x, shift, mask):
    i = 1
    y = x
    while i * shift < 32:
        z = y << shift
        y = x ^ (z & mask)
        i += 1
    return y


r = remote('crypto.zh3r0.cf', 4444)

values = []

for i in range(312):
    print(i)

    r.recvuntil("guess:\n")
    r.sendline(b"0")

    score = r.recvline().decode('utf-8').strip()
    print(score)

    p = r".* (\d+)\/(\d+).*"
    m = re.match(p, score)
    numerator = int(m.group(1))

    nmb = int(m.group(2))

    nmb *= 2**53 // numerator

    f_nmb = (nmb >> 26) << 5
    s_nmb = nmb & 0x3ffffff << 6
    values.append(untemper(s_nmb))
    values.append(untemper(f_nmb))

print(len(values))

mt_state = tuple([untemper(x) for x in values] + [624])
random.setstate((3, mt_state, None))

is_done = False

for j in range(2000 - i):
    if j % 100 == 0:
        print(j)
    r.recvuntil("guess:\n")

    ans = 0
    if not is_done:
        ans = random.getrandbits(53) / 2**53
    print(ans)
    r.sendline(str(ans).encode())

    result = r.recvline().decode('utf-8').strip()
    print(result)

    p = r"total score: (\d*).*"
    m = re.match(p, result)
    score = int(m.group(1))
    print(score)

    if score > 10**6:
        is_done = True

r.interactive()

# In [3]: random.random()
# Out[3]: 0.959231916338618
#
