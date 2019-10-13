from PIL import Image

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

def concat_tile(im, row, column):
    '''
    2次元の画像配列を受け取り，結合結果を返す
    '''
    dst_h = []
    for i in range(row):
        dst_h.append(concat_horizontal(im[i], column))
    return concat_vertical(dst_h, row)

W,H = 45,45

img = [[0]*W for _ in range(H)]
for i in range(W):
    for j in range(H):
        filename = 'picture/pieces/'+'{:04}'.format(W*i+j+1)+'.png'

        # 画像ファイルパスから読み込み
        im1 = Image.open(filename)
        img[i][j] = im1

concat_tile(img, W, H).save('concat_tile.png')
