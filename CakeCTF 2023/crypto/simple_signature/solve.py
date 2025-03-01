import os
import sys
from hashlib import sha512
from Crypto.Util.number import getRandomRange, getStrongPrime, inverse, GCD
import signal


flag = os.environ.get("FLAG", "neko{cat_does_not_eat_cake}")

p = getStrongPrime(512)
g = 2


def keygen():
    while True:
        x = getRandomRange(2, p-1)
        y = getRandomRange(2, p-1)
        w = getRandomRange(2, p-1)

        v = w * y % (p-1)
        if GCD(v, p-1) != 1:
            continue
        u = (w * x - 1) * inverse(v, p-1) % (p-1)
        return (x, y, u), (w, v)


def sign(m, key):
    x, y, u = key
    r = getRandomRange(2, p-1)

    return pow(g, x*m + r*y, p), pow(g, u*m + r, p)


def verify(m, sig, key):
    w, v = key
    s, t = sig

    return pow(g, m, p) == pow(s, w, p) * pow(t, -v, p) % p


def h(m):
    return int(sha512(m.encode()).hexdigest(), 16)


if __name__ == '__main__':
    magic_word = "cake_does_not_eat_cat"
    skey, vkey = keygen()

    p = 11173609363552764360591544657750495265984426112316117753742493340502706849223261526149408389159160831008072873912727490983417741225836440232729495047658779
    print(f"g = {g}")
    (s, t) = (4901696396160326308965548867517386990728039231827884692147852921240919374494695119984143004289455087033430302180993689906212586110792204289229354452034788, 4817622610365861511018824002897776742598717218200417591511605953113652840093051245923822476701292497372255077867185397600807517952767661543445823405691257)
    message = h("a")
    magic_message = h("cake_does_not_eat_cat")
    s_magic = pow(s, magic_message, p)
    t_magic = pow(t, magic_message, p)
    s_magic = pow(pow(s, magic_message, p), pow(message, -1, p-1), p)
    t_magic = pow(pow(t, magic_message, p), pow(message, -1, p-1), p)

    assert 2 <= s_magic < p
    assert 2 <= t_magic < p
    print(s_magic)
    print(t_magic)

