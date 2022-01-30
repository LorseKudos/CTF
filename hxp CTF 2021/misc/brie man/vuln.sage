#!/usr/bin/env sage
import re

if sys.version_info.major < 3:
    print('nope nope nope nope | https://hxp.io/blog/72')
    exit(-2)

rx = re.compile(r'Dear Bernhard: Your conjecture is false, for ([^ ]{,40}) is a counterexample\.')

s = CC.to_prec(160)(rx.match(input()).groups()[0])

r = round(s.real())
assert not all((s==r, r<0, r%2==0))     # boring

assert not s.real() == 1/2              # boring

assert zeta(s) == 0                     # uhm ok
print(open('flag.txt').read().strip())

