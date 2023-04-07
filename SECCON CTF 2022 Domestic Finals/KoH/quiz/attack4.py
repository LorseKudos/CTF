from typing import Optional
import secrets
import pickle
import os
import time

class LCG:
    def __init__(self, seed, m):
        self.a = 2
        self.seed = seed
        self.m = m

    def rand(self):
        self.seed = (self.seed * self.a) % self.m
        return self.seed

N = 65536 # public
# [1, ..., N]
ans = [(x+1) for x in range(N)]
# seed = int(secrets.token_hex(8), 16)
seed = 1
m = 27652344047805921227 # public int(secrets.token_hex(16), 16) * 2 + 1
lcg = LCG(seed, m)
while True:
    print(lcg.rand())
    time.sleep(0.1)
