import requests
import json
url = "http://witchquiz.dom.seccon.games/api/quiz/"

your_token = 'stspD3iyqv8pnRmS1Z9RPHUvRRL3R7iyFJgEiC_Xr5Y='
headers = {'Authorization': 'Token ' + your_token}

params = json.dumps({
  'answer': [0] * (1009*1009), # [required] your answer (Substituted into `your_answer` in the code)
  'stage': 1, # [required] this stage number. please use this value for this stage :)
  'tick': 963 # [optional] you can choose: 1 <= tick <= 113 && not yet submitted on that tick, If omitted, tick = 113 (current tick)
  })
res = requests.post(url, data=params, headers=headers)

# Returns 200 if accepted. otherwise returns not 200
if res.status_code == 200:
  print("success:", res.text)
else:
  print("error:", res.text)
