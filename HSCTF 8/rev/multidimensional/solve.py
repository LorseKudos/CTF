import numpy as np


def check(arr):
    s = ""
    for row in arr:
        for c in row:
            s += c
    return s


def check_rev(s):
    s_list = np.array(list(s))
    return s_list.reshape([6, 6]).tolist()


enc = "hey_since_when_was_time_a_dimension?"

assert check(check_rev(enc)) == enc

enc_rev1 = check_rev(enc)

print(enc_rev1)


def time(arr):
    t = [[8, 65, -18, -21, -15, 55],
         [8, 48, 57, 63, -13, 5],
         [16, -5, -26, 54, -7, -2],
         [48, 49, 65, 57, 2, 10],
         [9, -2, -1, -9, -11, -10],
         [56, 53, 18, 42, -28, 5]]
    for j in range(len(arr[0])):
        for i in range(len(arr)):
            arr[i][j] = chr(ord(arr[i][j]) + t[j][i])
    return arr


def time_rev(arr):
    t = [[8, 65, -18, -21, -15, 55],
         [8, 48, 57, 63, -13, 5],
         [16, -5, -26, 54, -7, -2],
         [48, 49, 65, 57, 2, 10],
         [9, -2, -1, -9, -11, -10],
         [56, 53, 18, 42, -28, 5]]
    for j in range(len(arr[0])):
        for i in range(len(arr)):
            arr[i][j] = chr(ord(arr[i][j]) - t[j][i])
    return arr


assert time(time_rev(enc_rev1)) == enc_rev1

enc_rev2 = time_rev(enc_rev1)


def space(arr):
    for n in range(36)[::-1]:
        arr[(35-n) // 6][(35-n) % 6] = chr(ord(arr[(35 - n) // 6]
                                               [(35 - n) % 6]) - (n // 6) - (n % 6))
    return arr


def space_rev(arr):
    for n in range(36):
        arr[(35-n) // 6][(35-n) % 6] = chr(ord(arr[(35 - n) // 6]
                                               [(35 - n) % 6]) + (n // 6) + (n % 6))
    return arr


assert space(space_rev(enc_rev2)) == enc_rev2

enc_rev3 = space_rev(enc_rev2)


def plane(arr):
    n = len(arr)
    for i in range(n // 2):
        for j in range(n // 2):
            t = arr[j][n - 1 - i]
            arr[j][n - 1 - i] = arr[n - 1 - i][n - 1 - j]
            arr[n - 1 - i][n - 1 - j] = arr[n - 1 - j][i]
            arr[n - 1 - j][i] = arr[i][j]
            arr[i][j] = t

    for i in range(n):
        for j in range(n):
            arr[i][j] = chr(ord(arr[i][j]) + i + n - j)

    return arr


def plane_rev(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n):
            arr[i][j] = chr(ord(arr[i][j]) - (i + n - j))

    for i in range(n // 2):
        for j in range(n // 2):
            t = arr[i][j]
            arr[i][j] = arr[n - 1 - j][i]
            arr[n - 1 - j][i] = arr[n - 1 - i][n - 1 - j]
            arr[n - 1 - i][n - 1 - j] = arr[j][n - 1 - i]
            arr[j][n - 1 - i] = t

    return arr


assert plane(plane_rev(enc_rev3)) == enc_rev3

enc_rev4 = plane_rev(enc_rev3)

print(enc_rev4)


def line(arr):
    newArr = [[""]*len(arr[0]) for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            p = i - 1
            q = j - 1
            f = 0
            row = i % 2 == 0
            col = j % 2 == 0
            if row:
                p = i + 1
                f += 1
            else:
                f -= 1
            if col:
                q = j + 1
                f += 1
            else:
                f -= 1
            newArr[p][q] = chr(ord(arr[i][j]) + f)
    return newArr


assert line(line(enc_rev4)) == enc_rev4

flag = line(enc_rev4)

print(flag)

print("".join(np.array(flag).T.flatten().tolist()))
