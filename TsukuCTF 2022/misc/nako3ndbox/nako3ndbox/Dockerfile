FROM python:3.10-alpine

RUN apk --no-cache add socat nodejs npm
RUN npm install -g nadesiko3@3.3.67

RUN adduser -D ctf

ADD app.nako3 /home/ctf/nako3ndbox/app.nako3
RUN chmod 500 /home/ctf/nako3ndbox/app.nako3
ADD flag.txt /home/ctf/nako3ndbox/flag.txt
RUN chmod 500 /home/ctf/nako3ndbox/flag.txt
RUN chown ctf:root /home/ctf -R

USER ctf
WORKDIR /home/ctf/nako3ndbox/

CMD socat TCP-L:31418,fork,reuseaddr EXEC:"cnako3 ./app.nako3",stderr