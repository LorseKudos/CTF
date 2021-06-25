import random
import time
import datetime
with open('output.txt') as (f):
    flag = list(f.read().strip())

for i in range(0, len(flag), 2):
    flag[i], flag[i + 1] = flag[(i + 1)], flag[i]


x = ['t', 'Y', 'w', 'V', '|', ']', 'u', 'X', '_', '0', 'P', 'k', 'h', 'D', 'A', '4', 'K', '5', 'z',
     'Z', 'G', '7', ';', 'S', ' ', '/', '6', '%', '}', '\\', ',', ':', '>', '#', 'a', '$', '3', '`',
     '+', 'R', 'b', 'H', 'd', 's', '1', 'J', 'L', 'v', '9', '2', 'o', 'M', '<', 'e', '(', 'x', '-',
     'B', 'm', "'", 'y', 'Q', '"', 'W', 'l', '.', 'i', 'O', '^', 'p', '8', 'f', 'F', 'C', '?', 'g',
     '@', 'j', '[', 'r', '!', '=', 'E', '~', '*', 'T', '{', ')', 'U', 'N', 'c', '&', 'n', 'q', 'I']

for _ in range(20):
    for i in range(len(flag)):
        flag[i] = chr(x.index(flag[i]) + 32)

d = datetime.datetime(2021, 4, 16, 4, 21, 0)
timestamp = int(time.mktime(d.timetuple()))

while True:
    flag_ck = flag[:]

    random.seed(timestamp)

    shuffle_rule = list(range(len(flag_ck)))
    random.shuffle(shuffle_rule)

    flag_ck_unshuffle = [0]*len(flag_ck)
    for after, before in enumerate(shuffle_rule):
        flag_ck_unshuffle[before] = flag_ck[after]
    flag_ck_unshuffle = "".join(flag_ck_unshuffle)

    if "flag{" in flag_ck_unshuffle:
        print(flag_ck_unshuffle)
        print(timestamp)
        break

    timestamp += 1
