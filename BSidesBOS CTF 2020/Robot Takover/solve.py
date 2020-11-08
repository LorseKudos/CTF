import requests
import re


def check(end_point, ua):
    global flag
    url = 'http://challenge.ctf.games:31879' + end_point

    headers = {'User-Agent': ua}
    response = requests.get(url, headers=headers)

    p = r'REJOICE, ROBOT. THE CHARACTER OF THE FLAG AT INDEX (.+) IS THE SAME CHARACTER AT INDEX (.+) IN THIS FILENAME.'
    m = re.match(p, response.text)
    if m:
        flag[int(m.group(1))] = end_point[int(m.group(2))+1]
        print(flag)
        print("".join(flag))


length = 1

flag = [""]*100

done_url = set()

while 1:
    url = 'http://challenge.ctf.games:31879/robots.txt'
    response = requests.get(url).text
    p_ua = r'User-agent: (.*)'
    p_da = r'Disallow: (.*)'

    for s in response.split('\n'):
        m_ua = re.match(p_ua, s)
        m_da = re.match(p_da, s)
        if m_ua:
            # print(m_ua.group(1))
            ua = m_ua.group(1)
        elif m_da:
            end_point = m_da.group(1)
            # print(end_point)
            if end_point not in done_url:
                done_url.add(end_point)
                check(end_point, ua)
