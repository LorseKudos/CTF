import socket


def recvuntil(s, tail):
    data = ''
    while True:
        if tail in data:
            return data
        data += s.recv(1).decode('utf-8')


def dijkstra(s, n, w, cost, open_time):
    d = [float("inf")] * n
    used = [False] * n
    d[s] = 0

    while True:
        v = -1
        for i in range(n):
            if (not used[i]) and (v == -1):
               v = i
            elif (not used[i]) and d[i] < d[v]:
                v = i
        if v == -1:
            break
        used[v] = True

        for j in range(n):
            d[j] = -(-min(d[j], d[v]+cost[v][j]) // open_time[j]) * open_time[j]
    return d


def get_ans(input_txt):
    n, w = map(int, input_txt[0].split())

    open_time = list(map(int, input_txt[1].split()))

    cost = [[10**10 for i in range(n)] for i in range(n)]

    for i in range(w):
        x, y, z = map(int, input_txt[i+2].split())
        cost[x-1][y-1] = z
        cost[y-1][x-1] = z

    start, goal = map(lambda x: int(x) - 1, input_txt[2+w].split())

    return dijkstra(start, n, w, cost, open_time)[goal]


if __name__ == '__main__':
    cnt = 0

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('142.93.113.55', 31085))

    recvuntil(s, 'runaway: ')
    s.sendall(("start\n").encode("utf-8"))

    try:
        while True:
            print(s.recv(1024).decode('utf-8'))
            receivedata = recvuntil(s, 'is: ')
            receivedata = receivedata.split('\n')
            print("[+]receivedata=", receivedata[1])

            if cnt > 0:
                receivedata = receivedata[2:]
            else:
                receivedata = receivedata[3:]

            ans = get_ans(receivedata)
            senddata = str(ans)
            print("[+]senddata=", senddata)
            s.sendall((senddata+"\n").encode("utf-8"))

            cnt += 1
    finally:
        receivedata = s.recv(1024).decode('utf-8')
        print(receivedata)
