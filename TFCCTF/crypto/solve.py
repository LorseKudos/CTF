import random
from pwn import *


def undo_state(states):
    N = 624
    M = 397
    MATRIX_A = 0x9908b0df
    UPPER_MASK = 0x80000000
    LOWER_MASK = 0x7fffffff
    mag01 = [0x0, MATRIX_A]

    for i in range(len(states))[::-1]:
        head = ((states[(i+N) % N] ^ states[(i+M) % N] ^
                mag01[states[(i+1) % N] & 0x1]) << 1) & UPPER_MASK
        tail = states[(i+N-1) % N] ^ states[(i+M-1) % N]
        body = ((tail ^ mag01[tail >> 31]) << 1) & LOWER_MASK
        states[i] = head ^ body ^ (tail >> 31)
    return states


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


if args.REMOTE:
    r = remote('01.linux.challenges.ctf.thefewchosen.com', 54248)
else:
    r = process("python3 main.py", shell=True)

random_values = []
for _ in range(78):
    r.recvuntil(b"> ")
    r.sendline(b"2")
    r.recvuntil(b"> ")
    r.sendline(b"0"*64)
    value = int(r.recvline().split()[-1], 16)
    print(value)
    for _ in range(8):
        print(value & 0xffffffff)
        random_values.append(value & 0xffffffff)
        value >>= 32

rand = random.Random()
mt_state = tuple([untemper(x) for x in random_values] + [624])
rand.setstate((3, mt_state, None))

r.recvuntil(b"> ")
r.sendline(b"2")
r.recvuntil(b"> ")
r.sendline(b"0"*64)
value = int(r.recvline().split()[-1], 16)
print(value)
print(rand.getrandbits(256))
