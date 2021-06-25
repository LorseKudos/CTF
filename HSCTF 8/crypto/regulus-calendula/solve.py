import sys
from pwn import *
import logging
from itertools import product

sys.setrecursionlimit(10000)


def _bits_to_int(bits, count):
    # Little endian.
    i = 0
    for k in range(count):
        i |= (bits[k] & 1) << k

    return i


def _branch_and_prune_pq(n, p, q, i):
    p_ = _bits_to_int(p, i)
    q_ = _bits_to_int(q, i)
    if i == len(p) or i == len(q):
        yield p_, q_
    else:
        c1 = ((n - p_ * q_) >> i) & 1
        p_prev = p[i]
        q_prev = q[i]
        p_possible = [0, 1] if p_prev is None else [p_prev]
        q_possible = [0, 1] if q_prev is None else [q_prev]
        for p_bit, q_bit in product(p_possible, q_possible):
            # Addition modulo 2 is just xor.
            if p_bit ^ q_bit == c1:
                p[i] = p_bit
                q[i] = q_bit
                yield from _branch_and_prune_pq(n, p, q, i + 1)

        p[i] = p_prev
        q[i] = q_prev


def factorize_pq(n, p_bits, q_bits):
    assert len(p_bits) == len(
        q_bits), "p and q bits should be of equal length."

    # Big endian to little endian.
    # Also make a copy to ensure we don't modify the original bits.
    p_bits = p_bits[::-1]
    q_bits = q_bits[::-1]

    # p and q are prime, odd.
    p_bits[0] = 1
    q_bits[0] = 1
    logging.debug("Starting branch and prune algorithm...")
    for p, q in _branch_and_prune_pq(n, p_bits, q_bits, 1):
        if p * q == n:
            return int(p), int(q)


if __name__ == "__main__":
    if args.REMOTE:
        r = remote("regulus-calendula.hsc.tf", 1337)
        r.recvuntil("with:\n")
        pow_cmd = r.recvline().strip().decode()
        r.recvuntil("? ")

        print(pow_cmd)

        r.interactive()
    else:
        r = process("python3 server.py", shell=True)

    print(r.recvuntil(": "))
    r.sendline("2")
    r.recvuntil(" = ")

    n = int(r.recvline().strip().decode('utf-8'))

    p1 = []

    for i in range(8):
        r.recvuntil(": ")
        r.sendline("4")
        r.recvuntil(": ")
        r.sendline(hex(i)[2:]*1024)

        p1.append(r.recvline().strip().decode("utf-8"))

    p2 = [" "]*1024

    for i in range(8):
        for s in range(1024):
            if p1[i][s] == "1":
                p2[s] = hex(i)[2:]

    q1 = []

    for i in range(8):
        r.recvuntil(": ")
        r.sendline("4")
        r.recvuntil(": ")
        r.sendline(hex(i)[2:]*1024)

        q1.append(r.recvline().strip().decode("utf-8"))

    q2 = [" "]*1024

    for i in range(8):
        for s in range(1024):
            if q1[i][s] == "1":
                q2[s] = hex(i)[2:]

    p3 = []

    for i in p2:
        if i == ' ':
            p3.extend([1, None, None, None])
        else:
            p3.extend([int(j) for j in list(bin(int(i))[2:].zfill(4))])

    q3 = []

    for i in q2:
        if i == ' ':
            q3.extend([1, None, None, None])
        else:
            q3.extend([int(j) for j in list(bin(int(i))[2:].zfill(4))])

    p, q = factorize_pq(n, p3, q3)
    d = pow(0x10001, -1, (p-1)*(q-1))

    r.recvuntil(": ")
    r.sendline("3")
    r.recvuntil(": ")
    r.sendline(str(d))
    r.recvline()

    r.interactive()
