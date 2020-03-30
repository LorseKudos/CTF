import random
import string

alphanum = string.ascii_letters + string.digits

c = ['00001001', '01011101', '00011000', '01010011', '00111101', '01100010', '01100000', '00011111', '00110101', '01100011', '01010101', '00110100', '01001011', '01011010',
     '01010101', '00110110', '01101100', '00111100', '01100001', '00011110', '00001011', '00001101', '00001000', '00000001', '01010110', '00111000', '00100101']


for s in range(1, 10000):
    random.seed(s)
    m = 'flag{'
    for i in range(5):
        if alphanum[random.randint(1, 1000) % len(alphanum)] != chr(ord(m[i]) ^ int(c[i], 2)):
            break
    else:
        print(s)
        seed = s
        break


def random_string(rand_seed, message):
    random.seed(rand_seed)
    rand_string = ''
    for i in range(len(message)):
        rand_string += alphanum[random.randint(1, 1000) % len(alphanum)]
    return rand_string


def decrypt(random_str, encrypt):
    message = ''
    for i in range(len(encrypt)):
        message += chr(int(encrypt[i], 2) ^ ord(random_str[i]))
    return message


print(decrypt(random_string(seed, c), c))
