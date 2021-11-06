import csv

bits = ""
with open('digital_ask.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for line in reader:
        bits += line[1]

s = ""
c = 0
for i in range(len(bits) // 16):
    val = int(bits[16*i])
    c = (c << 1) | val
    if i % 8 == 7:
        s = s + chr(c)
        c = 0

print(s)
