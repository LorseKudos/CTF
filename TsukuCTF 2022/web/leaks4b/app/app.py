import os
import re
import secrets
from flask import Flask, abort, request
from playwright.sync_api import sync_playwright

app = Flask(__name__)

FLAG = os.getenv("FLAG", "TsukuCTF22{dummy_flag}")

# コンテナで試す場合は要編集 (ex. http://host.docker.internal:31416, http://gateway.docker.internal:31416)
URL = "http://localhost:31416"

def cssi_sanitizer(text):
    # XSS could be mitigated by CSP, but CSSi and ReDoS are dangerous.
    deny_list = ["stylesheet", "import", "image", "style", "flag", "link", "img", "\"", "$", "'", "(", ")", "*", "+", ":", ";", "?", "@", "[", "\\", "]", "^", "{", "}"]
    text = text.lower()
    if any([hack in text for hack in deny_list]):
        return "ハッキングケーキ"
    return text

menu = ["チョコレートケーキ, チョコケーキ, chocolatecake", "チーズケーキ, cheesecake", "バナナケーキ, bananacake"]

@app.route("/<path:path>")
def missing_handler(path):
    abort(404, "ページが見つかりません。\nごめんね(^^♪")

@app.route("/")
def top():
    cake = request.args.get("cake", "チョコレートケーキ")
    cake = cssi_sanitizer(cake[:100])
    flag = request.cookies.get("flag")
    # It is not expected to steal the cookie.
    # This is "leaks4b."
    if (flag == FLAG) and (re.findall(cake, FLAG)):
        img = "flag0.jpg"
    elif re.findall(cake, menu[0]):
        img = f"cake0.jpg"
    elif re.findall(cake, menu[1]):
        img = f"cake1.jpg"
    elif re.findall(cake, menu[2]):
        img = f"cake2.jpg"
    else:
        img = f"cake3.jpg"
    nonce = secrets.token_urlsafe(16)
    return f"""<!doctype html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="Content-Security-Policy" content="script-src 'nonce-{nonce}'; base-uri 'none'; connect-src 'none'; font-src 'none'; form-action 'none'; frame-src 'none'; object-src 'none'; require-trusted-types-for 'script'; worker-src 'none';">
    <script src="https://cdn.tailwindcss.com" nonce="{nonce}"></script>
    <title>Leaks4b</title>
</head>
<body>
    <div class="bg-white py-6 sm:py-8 lg:py-12">
        <div class="max-w-screen-md px-4 md:px-8 mx-auto">
            <h1 class="text-gray-800 text-2xl sm:text-3xl font-bold text-center mb-4 md:mb-6">Leaks4b</h1>

            <p class="text-gray-500 sm:text-lg mb-6 md:mb-8">
                <span class="text-red-600">{cake}</span>を見せてあげます🍰<br>
                絶対に食べたらだめですからね！！<br>
            </p>

            <div class="bg-gray-100 overflow-hidden rounded-lg shadow-lg relative mb-6 md:mb-8">
            <img src="/static/img/{img}">
            </div>

            <p class="text-gray-500 sm:text-lg mb-6 md:mb-8">
                食べたければ<a href="/order" class="text-blue-600 font-bold">ここ</a>から注文してください。
            </p>


        </div>
    </div>
</body>
</html>
"""


@app.route("/order", methods=["GET"])
def order_get():
    nonce = secrets.token_urlsafe(16)
    return f"""<!doctype html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="Content-Security-Policy" content="script-src 'nonce-{nonce}'; base-uri 'none'; connect-src 'none'; font-src 'none'; frame-src 'none'; object-src 'none'; require-trusted-types-for 'script'; worker-src 'none';">
    <script src="https://cdn.tailwindcss.com" nonce="{nonce}"></script>
    <title>Leaks4b</title>
</head>
<body>
    <div class="bg-white py-6 sm:py-8 lg:py-12">
        <div class="max-w-screen-md px-4 md:px-8 mx-auto">
            <h1 class="text-gray-800 text-2xl sm:text-3xl font-bold text-center mb-4 md:mb-6">Leaks4b<br> ~ Cake Order Page ~</h1>

            <p class="text-gray-500 sm:text-lg mb-6 md:mb-8">
                以下から注文したいケーキのURLを送信してください。<br>
                ただし、パティシエは忙しいので大量の注文はやめてください。  
            </p>

            <form method="post" class="form">
            <div class="mb-6">
                <label class="text-gray-500 sm:text-lg mb-6 md:mb-8">URL</label>
                <input type="url" name="url" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5" placeholder="{URL}" required>
            </div>
            <button type="submit" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Order</button>
            </form>

        </div>
    </div>
</body>
</html>
"""

@app.route("/order", methods=["POST"])
def order_post():
    url = request.form.get("url", "____")
    if not url.startswith("http"):
        return "[ERROR] http and https schemes are allowed."
    try:
        with sync_playwright() as p:
            browser = p.firefox.launch()
            context = browser.new_context()
            context.add_cookies([{"name": "flag", "value": FLAG, "httpOnly": True, "url": URL}])
            page = context.new_page()
            page.goto(url, timeout=10000)
            browser.close()
    except Exception as e:
        print(e)
        pass
    return "I received your cake order. Have the flag and wait for your cake!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=31416)
    # ソース汚くてゴメンね(´;ω;｀)