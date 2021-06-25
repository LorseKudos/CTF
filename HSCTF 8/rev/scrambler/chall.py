import random
import time
with open('flag.txt') as (f):
    flag = list(f.read())

if len(flag) % 2 == 1:
    flag.append(' ')
x = ['t', 'Y', 'w', 'V', '|', ']', 'u', 'X', '_', '0', 'P', 'k', 'h', 'D', 'A', '4', 'K', '5', 'z',
     'Z', 'G', '7', ';', 'S', ' ', '/', '6', '%', '}', '\\', ',', ':', '>', '#', 'a', '$', '3', '`',
     '+', 'R', 'b', 'H', 'd', 's', '1', 'J', 'L', 'v', '9', '2', 'o', 'M', '<', 'e', '(', 'x', '-',
     'B', 'm', "'", 'y', 'Q', '"', 'W', 'l', '.', 'i', 'O', '^', 'p', '8', 'f', 'F', 'C', '?', 'g',
     '@', 'j', '[', 'r', '!', '=', 'E', '~', '*', 'T', '{', ')', 'U', 'N', 'c', '&', 'n', 'q', 'I']
timestamp = int(time.time())
random.seed(timestamp)
for _ in range(20):
    for i in range(len(flag)):
        flag[i] = x[(ord(flag[i]) - 32)]
else:
    random.shuffle(flag)

for i in range(0, len(flag), 2):
    flag[i], flag[i + 1] = flag[(i + 1)], flag[i]
else:
    print(''.join(flag))
