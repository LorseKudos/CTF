# coding: utf-8
import random
import os

flag = b"ctf4b{"
cipher = [4396, 22819, 47998, 47995, 40007, 9235, 21625, 25006, 4397, 51534, 46680, 44129, 38055, 18513, 24368, 38451, 46240, 20758, 37257, 40830, 25293,
          38845, 22503, 44535, 22210, 39632, 38046, 43687, 48413, 47525, 23718, 51567, 23115, 42461, 26272, 28933, 23726, 48845, 21924, 46225, 20488, 27579, 21636]

for i in range(5, len(cipher)):
    for c in range(127):
        if ((flag[i] + c) ** 2 + i) in cipher:
            flag += chr(c).encode()

print(flag)
# b'ctf4b{hi_b3g1nner!g00d_1uck_4nd_h4ve_fun!!!}'
