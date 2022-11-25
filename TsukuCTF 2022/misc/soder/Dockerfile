FROM python:3.10-alpine

RUN apk --no-cache add socat py3-pip
RUN pip3 install timeout_decorator
RUN adduser -D ctf

ADD soder.py /home/ctf/soder/soder.py
RUN chmod 500 /home/ctf/soder/soder.py
RUN chown ctf:root /home/ctf -R

USER ctf
WORKDIR /home/ctf/soder/
CMD socat TCP-L:31417,fork,reuseaddr EXEC:"python3 ./soder.py",stderr