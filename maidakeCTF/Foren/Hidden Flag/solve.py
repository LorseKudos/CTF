from PIL import Image
import os

base = os.path.dirname(os.path.abspath(__file__))
name = os.path.normpath(os.path.join(base, 'flag.png'))
img = Image.open(name)

w, h = img.size

rule = {
    1: [[' ', '2', '7', 'c', 'h'],
        ['.', '3', '8', 'd', 'i'],
        ['?', '4', '9', 'e', 'j'],
        ['0', '5', 'a', 'f', 'k'],
        ['1', '6', 'b', 'g', 'l']],
    2: [['m', 'r', 'w', 'B', 'G'],
        ['n', 's', 'x', 'C', 'H'],
        ['o', 't', 'y', 'D', 'I'],
        ['p', 'u', 'z', 'E', 'J'],
        ['q', 'v', 'A', 'F', 'K']],
    3: [['L', 'Q', 'V', '[', '`'],
        ['M', 'R', 'W', '¥', '{'],
        ['N', 'S', 'X', ']', '|'],
        ['O', 'T', 'Y', '^', '}'],
        ['P', 'U', 'Z', '_', '!']]}

length = 30

flag = ""
i = 0
for x in range(w):
    for y in range(h):
        r, g, b, a = img.getpixel((x, y))
        print(r, g, b, a)
        try:
            flag += rule[r][b][g]
            i+=1
        except (KeyError, IndexError):
            continue
        if i == length:
            break
    if i == length:
        break

print(flag)
