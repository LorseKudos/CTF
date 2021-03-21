from pwn import *
import itertools

r = remote('20.48.84.64', 20001)

for game_cnt in range(15):
    print(game_cnt)
    r.recvuntil("Creating a new problem...\n")

    while True:
        stones = list(map(int, r.recvline().split()))
        num_heap = len(stones)

        r.recvuntil(": ")

        for i, j in itertools.product(range(num_heap), range(1, 4)):
            if stones[i] < j:
                continue
            tmp_stones = stones[:]
            tmp_stones[i] -= j
            cnt = 0
            for s in tmp_stones:
                cnt ^= s
            if cnt % 4 == 0:
                remove_idx = i
                remove_num = j

        if len(stones) != 1:
            r.sendline(str(remove_idx))
            r.recvuntil(": ")

        r.sendline(str(remove_num))
        text = r.recvline().decode()
        if "Won!" in text:
            break
r.interactive()
