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


r = remote('archive.cryptohack.org', 46347)

values1 = []
for _ in range(624):
    a = int(r.recvline().decode('utf-8').strip())
    values1.append(a)

mt_state = [untemper(x) for x in values1]
mt_state = undo_state(mt_state)

ans = b""
for state in mt_state:
    ans += state.to_bytes(4, 'big')

if b"zh3r0{" in ans:
    ans = ans[ans.index(b"zh3r0{"):]
    ans = ans[:ans.index(b"}")+1]
    print(ans)
