from Crypto.PublicKey import RSA
import gmpy2
import binascii

def continued_fraction(n, d):
    """
    415/93 = 4 + 1/(2 + 1/(6 + 1/7))

    >>> continued_fraction(415, 93)
    [4, 2, 6, 7]
    """
    cf = []
    while d:
        q = n // d
        cf.append(q)
        n, d = d, n-d*q
    return cf

def convergents_of_contfrac(cf):
    """
    4 + 1/(2 + 1/(6 + 1/7)) is approximately 4/1, 9/2, 58/13 and 415/93

    >>> list(convergents_of_contfrac([4, 2, 6, 7]))
    [(4, 1), (9, 2), (58, 13), (415, 93)]
    """
    n0, n1 = cf[0], cf[0]*cf[1]+1
    d0, d1 = 1, cf[1]
    yield (n0, d0)
    yield (n1, d1)

    for i in range(2, len(cf)):
        n2, d2 = cf[i]*n1+n0, cf[i]*d1+d0
        yield (n2, d2)
        n0, n1 = n1, n2
        d0, d1 = d1, d2

def wieners_attack(e, n):
    cf = continued_fraction(e, n)
    convergents = convergents_of_contfrac(cf)

    for k, d in convergents:
        if k == 0:
            continue
        phi, rem = divmod(e*d-1, k)
        if rem != 0:
            continue
        s = n - phi + 1
        # check if x^2 - s*x + n = 0 has integer roots
        D = s*s - 4*n
        if D > 0 and gmpy2.is_square(D):
            return d

if __name__ == '__main__':
    pubkey = RSA.importKey(open("pubkey.pem").read())
    e = pubkey.e
    n = pubkey.n



    print("e :", e)
    print("n :", n)
    d = wieners_attack(e, n)
    print("found d: %d" % d)
    m = pow(c, d, n)
    print(m)
    flag = binascii.unhexlify(format(m, 'x')).decode()
    print(flag)
