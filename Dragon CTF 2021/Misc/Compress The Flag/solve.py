
from pwn import *
import random
from string import ascii_uppercase


def main():
    r = remote('compresstheflag.hackable.software', 1337)

    FLAG = b"DrgnS{" + b'A'*18 + b"}"

    seed = 2000000000
    while True:
        flag = bytearray(FLAG)
        random.seed(seed)
        random.shuffle(flag)
        if flag[:4] == b"Drgn":
            print(seed)
            break
        seed += 1

    seed = str(seed)
    flag = "Drgn"

    r.recvuntil(b"DrgnS{[A-Z]+}\n")
    for _ in range(21):
        m = 9999
        for c in " " + ascii_uppercase + "{}":
            r.sendline(f"{seed}:{(flag + c)*10}")
            res = r.recvlines(5)
            zlib_res = int(res[1][-2:].decode('utf-8'))

            if zlib_res < m:
                m = zlib_res
                mf = flag + c
        flag = mf
        print(flag)

    rule = list(range(25))
    random.seed(int(seed))
    random.shuffle(rule)
    shuffled_flag = flag
    flag = [""]*25

    for i in range(len(shuffled_flag)):
        flag[rule[i]] = shuffled_flag[i]

    print("".join(flag))

if __name__ == "__main__":
    main()
