def make_table(key, table):
    length = len(key)
    temp = 0

    for i in range(0x100):
        table[i] = i

    for i in range(0x100):
        var2 = table[i] + temp + key[i % length]
        var1 = (var2 >> 0x1f) >> 0x18
        temp = (var2 + var1 & 0xff) - var1
        table[i], table[temp] = table[temp], table[i]


key = [0x72, 0x67, 0x55, 0x41, 0x76, 0x76, 0x79, 0x66, 0x79, 0x41, 0x70, 0x4e, 0x50, 0x45, 0x59, 0x67]

table = [""]*256

make_table(key, table)

print(table)

def encrypt(table, message):
    temp = local_20 = 0
    length = len(message)
    enc_message = ""

    for i in range(length):
        temp = (temp + 1) & 0xff
        local_20 = (table[temp] + local_20) & 0xff
        table[temp], table[local_20] = table[local_20], table[temp]
        enc_message += chr(message[i] ^ table[table[local_20] + table[temp]])

encrypt(table, b"ctf4b{")
