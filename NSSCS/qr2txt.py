from PIL import Image

BLACK = 'X'
WHITE = '_'
UNKNOWN = '?'

quiet_zone_size = 16
cell_size = 4
unknown_cols = 18

img = Image.open('composition.png').convert('RGB')

w, h = img.size

qrtxt = ''

y = quiet_zone_size + cell_size - 1

while y < h - quiet_zone_size:
    x = quiet_zone_size + cell_size - 1
    while x < w - quiet_zone_size:
        r, g, b = img.getpixel((x, y))
        
        if x < quiet_zone_size + cell_size * unknown_cols:
            qrtxt += UNKNOWN
        elif r == 0 and g == 0 and b == 0:
            qrtxt += BLACK
        else:
            qrtxt += WHITE
        x += cell_size
    qrtxt += '\n'
    y += cell_size

with open('qr.txt', 'w') as f:
    f.write(qrtxt)