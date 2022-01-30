# Running locally:
# 1) echo 'hxp{FLAG}' > flag.txt
# 2) docker build -t brie_man .
# 3) docker run -p 7904:1024 --rm --cap-add=SYS_ADMIN --security-opt apparmor=unconfined -it brie_man

FROM archlinux

RUN pacman -Sy --noconfirm sagemath

RUN useradd --create-home --shell /bin/bash ctf
WORKDIR /home/ctf

COPY ynetd /sbin/

COPY vuln.sage flag.txt /home/ctf/

USER ctf
RUN sage --nodotsage -preparse ./vuln.sage  # creates vuln.sage.py

USER root

# sane defaults
RUN chmod 555 /home/ctf && \
    chown -R root:root /home/ctf && \
    chmod -R 000 /home/ctf/* && \
    chmod 500 /sbin/ynetd

RUN chmod 555 vuln.sage && \
    chmod 555 vuln.sage.py && \
    chmod 444 flag.txt

# check whitelist of writable files/folders
RUN find / -ignore_readdir_race -type f \( -perm -4000 -o -perm -2000 \) -not -wholename /readflag -delete
USER ctf
RUN (find --version && id --version && sed --version && grep --version) > /dev/null
RUN ! find / -writable -or -user $(id -un) -or -group $(id -Gn|sed -e 's/ / -or -group /g') 2> /dev/null | grep -Ev -m 1 '^(/dev/|/run/|/proc/|/sys/|/tmp|/var/tmp|/var/lock|/var/mail|/var/spool/mail)'
USER root

EXPOSE 1024
CMD ynetd -u ctf -lt 10 -t 60 -lm 4294967296 -sh y "HOME=/home/ctf sage --nodotsage -python /home/ctf/vuln.sage.py"
