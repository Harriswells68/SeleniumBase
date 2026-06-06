# raw__turnstile.py
from seleniumbase import sb_cdp
import random
from seleniumbase import SB
import requests
import re
import time
import os

os.makedirs("screenshots", exist_ok=True)


def generate_vlink(c):
    k=0

    while k<10:
        url = f"https://api.catchmail.io/api/v1/mailbox?address=ytprojectelevenlabsacckbkb{c}@catchmail.io"
        r = requests.request("GET", url).json()
        if r["count"]>0:
            url = f"https://api.catchmail.io/api/v1/message/{r["messages"][0]["id"]}?mailbox=ytprojectelevenlabsacckbkb{c}@catchmail.io"
            r = requests.request("GET", url).json()

            return re.findall(r"(https?://[^\s)]+)(?=\s\))", (r["body"]["text"]))[1]        
        else:
            k+=1
            time.sleep(4)
    
    raise Exception("ERRROR")

url = "https://scrapfly.io/web-scraping-tools/automation-detector"

w=random.randint(9999, 12000)

print(w)

try:
    sb = sb_cdp.Chrome(url,
    headed=True, 
    chromium_arg="--no-sandbox")

    sb.sleep(4000)

    
finally:
    sb.driver.stop()
