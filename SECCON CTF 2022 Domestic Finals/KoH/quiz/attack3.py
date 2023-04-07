import requests
import json
import time

url = "http://witchquiz.dom.seccon.games/api/quiz/"

your_token = 'stspD3iyqv8pnRmS1Z9RPHUvRRL3R7iyFJgEiC_Xr5Y='
headers = {'Authorization': 'Token ' + your_token}



prev_score = 2030156
payload_static = [0] * (1009*1009)
# for query_number in range(1000000):

payload = payload_static[:]

tick_init = 491
l = 0
r = 504
print("# of change:", r-l)
for i in range(l, r):
    payload[i * 1009] = 1

params = json.dumps({
'answer': payload, # [required] your answer (Substituted into `your_answer` in the code)
'stage': 3, # [required] this stage number. please use this value for this stage :)
'tick': tick_init # [optional] you can choose: 1 <= tick <= 107 && not yet submitted on that tick, If omitted, tick = 107 (current tick)
})

res = requests.post(url, data=params, headers=headers)



# Returns 200 if accepted. otherwise returns not 200
if res.status_code == 200:
    print("success:", res.text)
    score = res.json()["score"]
    print("score_diff:", (prev_score - score)/2)    # incr
    if prev_score < score:
        prev_score = score
        #print(payload)
    # keep
    elif prev_score == score:
        payload_static[query_number] = 2
        prev_score = score
        #print(payload)
    else:
        pass

else:
    print("error:", res.text)


time.sleep(5)
