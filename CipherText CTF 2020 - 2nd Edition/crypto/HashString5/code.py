import hashlib
from random import randint
from string import ascii_letters

flag = "CTCTF{hoge}"

permuted_flag = ''

for i, j in enumerate(flag):
    if i % 2:
        permuted_flag = f'{permuted_flag}{j}{ascii_letters[randint(1,len(ascii_letters)-1)]}'
    else:
        permuted_flag = f'{j}{permuted_flag}{ascii_letters[randint(1,len(ascii_letters)-1)]}'

permuted_flag = permuted_flag.strip()

print(permuted_flag)

hashed_flag = ''.join([hashlib.md5(i.encode()).hexdigest() for i in permuted_flag])

print(hashed_flag)

