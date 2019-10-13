from PIL import Image

WH_LEN = 180
UNIT_SIZE = 4

IFILE_FORMAT = './pieces/%04d.png'

output_img = Image.new('RGB', (WH_LEN, WH_LEN), (255, 255, 255))

x = 0
y = 0

for i in range((WH_LEN / UNIT_SIZE) * (WH_LEN / UNIT_SIZE)):
    filename = IFILE_FORMAT % (i + 1)
    input_img = Image.open(filename).convert('RGB')
    if x == WH_LEN / UNIT_SIZE:
        x = 0
        y += 1
    output_img.paste(input_img, ((x * UNIT_SIZE), (y * UNIT_SIZE)))
    x += 1
        
output_img.save('composition.png')