curl -XPOST https://post.web.wanictf.org/chal/1 -d "data=hoge"
curl -XPOST https://post.web.wanictf.org/chal/2 -d "data=hoge" -H "user-agent: Mozilla/5.0"
curl -XPOST https://post.web.wanictf.org/chal/3 -H "Content-Type: application/json" -d '{"data": {"hoge":"fuga"}}'
curl -XPOST https://post.web.wanictf.org/chal/4 -H "Content-Type: application/json" -d '{"hoge": 1, "fuga": null}'
curl -XPOST https://post.web.wanictf.org/chal/5 -F "data=@app/public/images/wani.png"

# ./solve.sh | grep FLAG
