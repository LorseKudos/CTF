import random
import string
from deep_memory import message

print("Encrpyt everything!!.... Oh no, system failure. Encrypting last message received")

rand = random.randint(1, 10000)
alphanum = string.ascii_letters + string.digits

encrypt = ['00001001', '01011101', '00011000', '01010011', '00111101', '01100010', '01100000', '00011111', '00110101', '01100011', '01010101', '00110100', '01001011', '01011010',
           '01010101', '00110110', '01101100', '00111100', '01100001', '00011110', '00001011', '00001101', '00001000', '00000001', '01010110', '00111000', '00100101']


def random_string(rand_seed, message):
    random.seed(rand_seed)
    rand_string = ''
    for i in range(len(message)):
        rand_string += alphanum[random.randint(1, 1000) % len(alphanum)]
    return rand_string


def encrpyt(random_str, message):
    encrpyted = ''
    for i in range(len(message)):
        k = ord(message[i]) ^ ord(random_str[i])
        encrpyted += (bin(k)[2:]).zfill(8)
    return encrpyted


print(encrpyt(random_string(rand, message), message))
