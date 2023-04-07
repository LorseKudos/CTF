import requests
import json
import time
url = "http://witchquiz.dom.seccon.games/api/quiz/"

your_token = 'stspD3iyqv8pnRmS1Z9RPHUvRRL3R7iyFJgEiC_Xr5Y='
headers = {'Authorization': 'Token ' + your_token}

N = 65536

for number in range(10000):
  ans = [1]*(N//6) + [2]*(N//6) + [3]*(N//6) + [4]*(N//6) + [5]*(N//6 + (N%6))
  params = json.dumps({
    'answer': ans, # [required] your answer (Substituted into `your_answer` in the code)
    'stage': 4, # [required] this stage number. please use this value for this stage :)
    'tick': 282 + number # [optional] you can choose: 1 <= tick <= 113 && not yet submitted on that tick, If omitted, tick = 113 (current tick)
    })
  res = requests.post(url, data=params, headers=headers)

  # Returns 200 if accepted. otherwise returns not 200
  if res.status_code == 200:
    print("success:", res.text)
    score = res.json()["score"]
    print(score)
  else:
    print("error:", res.text)
  time.sleep(5)
