from PIL import Image
import os
import numpy as np
import pytesseract
import zipfile


for i in reversed(range(51)):
    base = os.path.dirname(os.path.abspath(__file__))
    name = os.path.normpath(os.path.join(base, './tmp/password.png'))
    img = np.array(Image.open(name))

    with open(os.path.normpath(os.path.join(base, './tmp/shift_keys'))) as f:
        keys = list(map(int, f.read().strip().split("\n")))

    for w in range(len(img)):
        img[w] = np.concatenate([img[w][keys[w]:], img[w][:keys[w]]])

    pil_img = Image.fromarray(img)
    pwd = pytesseract.image_to_string(pil_img).strip()
    print(pwd)

    filename = os.path.normpath(os.path.join(base, f'./tmp/UnzipME{i}.zip'))
    path = os.path.normpath(os.path.join(base, './tmp'))
    with zipfile.ZipFile(filename, 'r') as zip_file:
        try:
            zip_file.extractall(path=path, pwd=pwd.encode('utf-8'))
            print('extraction is successful!')
        except RuntimeError:
            print('{} is wrong password!'.format(pwd))
