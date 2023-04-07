with open("spi.txt", "r") as f:
    packet = f.readlines()

datas = [""]*64

for line in packet:
    line = line.strip()
    direction = line.split(" : ")[0]
    payload = line.split(" : ")[1]
    if direction == "Device to SD Card":
        if payload.startswith("51"):
            offset = int(payload[2:-2], 16)
    else:
        if payload.startswith("ff"):
            data = bytes.fromhex(payload.split("fe", 1)[1][:-4])
            datas[offset] = data

image = b""
for data in datas:
    image += data

with open("flag.jpeg", "wb") as f:
    f.write(image)
# ACSC{1tW@sE@syW@snt1t}
