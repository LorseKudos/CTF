from hashlib import *
import random
import string
(m, n, x_head, y_head) = (300, 12, 'igg', 'dead')

print(m, n, x_head, y_head)

while True:
    x = x_init = x_head + ''.join([random.choice(string.printable[:-6])
                                   for i in range(16)])
    xhash = ""
    for _ in range(m - n):
        xhash = md5(x.encode('utf-8')).hexdigest()
        x = xhash
    if xhash.startswith(y_head):
        break

print(x_init, xhash)
