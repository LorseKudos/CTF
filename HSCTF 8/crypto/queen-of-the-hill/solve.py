import numpy

alphabet = "abcdefghijklmnopqrstuvwxyz"
N = len(alphabet)

matrix = [[16, 25, 8],
          [14, 19, 5],
          [15, 17, 3]]

ciphertext = "rtcavbuhpkaiqgfjnxrdaujw"

# cf: http://arc360.info/algo/privatekey.html


def euclidean(x, y):
    x1 = 1
    y1 = 0
    z1 = x
    x2 = 0
    y2 = 1
    z2 = y

    while z2 != 1:
        q = (z1 - (z1 % z2)) / z2
        x1 = x1 - q * x2
        y1 = y1 - q * y2
        z1 = z1 - q * z2

        x1, y1, z1, x2, y2, z2 = x2, y2, z2, x1, y1, z1

    while x2 < 0:
        x2 += y

    return x2


alphabet_to_number = {}

for i in range(0, len(alphabet)):
    alphabet_to_number[alphabet[i]] = i

# https://www.youtube.com/watch?v=LhBovzm4Ajs
det = numpy.around(numpy.linalg.det(matrix)).astype(numpy.int64)
inv = numpy.around(det * numpy.linalg.inv(matrix)).astype(numpy.int64)

mul = euclidean(det, N)
inv = mul * inv

for i in range(0, len(inv)):
    for j in range(0, len(inv[i])):
        inv[i][j] = inv[i][j] % N

ans = ''

for j in range(0, 8):
    cipherarray = []
    for i in range(0, len(inv)):
        if 'a' <= ciphertext[j * len(inv) + i] <= 'z':
            cipherarray.append(alphabet_to_number[ciphertext[j * len(inv) + i]])
        else:
            cipherarray.append(alphabet_to_number[ciphertext[j * len(inv) + i]])
    plain = numpy.dot(inv, cipherarray)
    print(plain)

    for i in range(0, len(plain)):
        print(alphabet[int(plain[i]) % N])
        ans += alphabet[int(plain[i]) % N]

print(ans)
