import socket
import re

from datetime import datetime as dt, timedelta

def get_ans(start_date, end_date):
    ans = 0
    diff = (end_date - start_date).days + 1

    for i in range(diff):
        date = start_date + timedelta(i)
        cnt = 0
        for c in date.strftime('%Y%m%d'):
            if 1 <= int(c) <= 4:
                cnt += 1

        if cnt == 5:
            ans += 1

    return ans

def recvuntil(s, tail):
    data = ''
    while True:
        if tail in data:
            return data
        data += s.recv(1).decode('utf-8')


if __name__ == '__main__':

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('nssc-stu.mydns.jp', 41016))
    while True:
        receivedata = s.recv(1024).decode('utf-8')
        print("[+]receivedata=",receivedata[2:])
        receivedata = s.recv(1024).decode('utf-8')
        print("[+]receivedata=",receivedata)
        pattern = r'''START:(.*)
  END  :(.*)'''
        m1 = re.findall(pattern,receivedata)[0]

        start_date, end_date = map(lambda d: dt.strptime(d.rstrip() ,"%Y/%m/%d") ,m1)
        print(start_date, end_date)

        ans = get_ans(start_date, end_date)
        print("[+]ans=",ans)
        senddata = str(ans)
        print("[+]senddata=",senddata)
        s.sendall((senddata+"\n").encode("utf-8"))
        # receivedata = recvuntil(s, "\n")
        # print("[+]receivedata=",receivedata)
