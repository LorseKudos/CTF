# coding: utf-8

N = int(input())
beatmap = [input()[1:-1] for _ in range(N)]

ans = beatmap[0].count('-')
for i in range(1,N):
    for j in range(len(beatmap[i])):
        if beatmap[i][j] == '-' and beatmap[i-1][j] != '#':
            ans += 1

print(ans)
