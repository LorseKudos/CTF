from flask import (
    Flask,
    abort,
    make_response,
    render_template,
    request,
    redirect
)
import redis
import pycurl
from io import BytesIO
import traceback
import uuid
import json

app = Flask(__name__)

# initialization
redis = redis.Redis(host='redis', port=6379, db=0)
flag = "TsukuCTF22{dummy flag}" # the flag is replaced a real flag in a production environment.
id = str(uuid.uuid4())
redis.set(id, json.dumps({"id": id, "name": flag}))

# only 'http' and 'https' should have been allowed, right?
# ref: https://everything.curl.dev/cmdline/urls/scheme#supported-schemes
blacklist_of_scheme = ['dict', 'file', 'ftp', 'gopher', 'imap', 'ldap', 'mqtt', 'pop3', 'rtmp', 'rtsp', 'scp', 'smb', 'smtp', 'telnet']

def url_sanitizer(uri: str) -> str:
    if len(uri) == 0 or any([scheme in uri for scheme in blacklist_of_scheme]):
        return "https://fans.sechack365.com"
    return uri

# a response is also sanitized just in case because the flag is super sensitive information.
blacklist_in_response = ['TsukuCTF22']

def response_sanitizer(body: str) -> str:
    if any([scheme in body for scheme in blacklist_in_response]):
        return "SANITIZED: a sensitive data is included!"
    return body

@app.route("/<path:path>")
def missing_handler(path):
    abort(404, "ページが見つかりません")

@app.route("/", methods=["GET", "POST"])
def route_index():
    session_id = request.cookies.get('__SESSION_ID')
    name = None
    if session_id is not None:
        res= redis.get(session_id)
        if res is not None:
            user = json.loads(res)
            print(f"user: {user}")
            name = user["name"]
            if name is not None and "TsukuCTF22{" in name:
                name = "tsukushi"
    else:
        return redirect('/register')

    if request.method == "POST":
        url = url_sanitizer(request.form.get("url"))

        buf = BytesIO()
        try:
            c = pycurl.Curl()
            c.setopt(c.URL, url)
            c.setopt(c.WRITEDATA, buf)
            c.perform()
            c.close()
    
            body = buf.getvalue().decode('utf-8')
        except Exception as e:
            traceback.print_exc()
            abort("error occurs")
        return render_template("index.html", url=url, data=response_sanitizer(body), name=name)
    return render_template("index.html", data=None, name=name)

@app.route("/register", methods=["GET"])
def register():
    return render_template("register.html")
    

@app.route("/register", methods=["POST"])
def register_post():
    name = request.form.get("name")
    redis.set(id, json.dumps({"id": str(uuid.uuid4()), "name": name}))
    redis.expire(id, 100)
    
    resp = make_response(redirect('/'))
    resp.set_cookie('__SESSION_ID', id)
    return resp

@app.route("/logout", methods=["GET"])
def logout():
    resp = make_response(redirect('/'))
    resp.set_cookie('__SESSION_ID', '', expires=0)
    return resp

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=31555)
