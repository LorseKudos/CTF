from PIL import Image
from Crypto.Util.number import bytes_to_long


def concat_horizontal(im, column):
    '''
    画像配列を受け取り，横方向に結合し，結合画像を返す
    '''
    dst = Image.new('RGB', (im[0].width * column, im[0].height))
    for x in range(column):
        dst.paste(im[x], (x * im[0].width, 0))
    return dst


def concat_vertical(im, row):
    '''
    画像配列を受け取り，縦方向に結合し，結合画像を返す
    '''
    dst = Image.new('RGB', (im[0].width, im[0].height * row))
    for y in range(row):
        dst.paste(im[y], (0, y * im[0].height))
    return dst


W, H = 300, 300

img = [0]*W
image = []
for i in range(W):
    for j in range(H):
        filename = 'image/'+str(bytes_to_long(f'{i} {j}'.encode()))+'.jpg'

        im1 = Image.open(filename)
        img[j] = im1
    image.append(concat_horizontal(img, H))
    print(i)

concat_vertical(image, W).save('concat_tile.jpg')
