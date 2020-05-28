o = "AKeyFor" + "ios" + "10.3"
xored = [34, 63, 3, 77, 36, 20, 24, 8, 25, 71, 110, 81, 64, 87, 30, 33, 81, 15, 39, 90, 17, 27]
l = "ctf4b{"

for i in range(len(xored)):
    print(chr(xored[i] ^ ord(o[i % len(o)])), end="")
