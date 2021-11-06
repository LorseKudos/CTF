from Crypto.Util.number import long_to_bytes

with open("output.txt", "r") as f:
    enc = int(f.read())

print(long_to_bytes(enc))
