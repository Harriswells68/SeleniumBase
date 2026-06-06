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

sb = sb_cdp.Chrome(
    "https://headless-detector.vercel.app/",
    test=True,
    guest_mode=True
)

sb.sleep(4)

sb.save_as_pdf("example_page.png", folder="screenshots") 

sb.save_screenshot("after sign up.png", "screenshots")

# url = "https://elevenlabs.io/app/sign-up"

# w=random.randint(9999, 12000)

# print(w)

# sb = sb_cdp.Chrome(
#     url,
#     test=True,
#     guest_mode=True
# )

# try:
#     sb.sleep(4)

#     sb.press_keys('input[name="email"]', f"ytprojectelevenlabsacckbkb{9990+w}@catchmail.io")  # human-speed
#     sb.press_keys('input[name="password"]', "Prince!4438#")

#     # Standard syntax for clicking a button containing specific text in  Mode
#     sb.gui_click_element('div[data-testid="signup-signup-button-div"] button:contains("Sign up")')

#     sb.sleep(0.2)

#     sb.solve_captcha()

#     sb.sleep(2)

#     sb.save_screenshot("after sign up.png", "screenshots")

#     sb.sleep(4)

#     sb.save_screenshot("after sign up after 2.png", "screenshots")

#     link=generate_vlink(9990+w)

#     sb.open(link)

#     sb.sleep(5)

#     sb.click('button:contains("Continue")')

#     sb.sleep(1)

#     sb.press_keys('input[name="password"]', "Prince!4438#")

#     sb.save_screenshot("before sign in.png", "screenshots")

#     sb.sleep(1)

#     # Standard syntax for clicking a button containing specific text in  Mode
#     sb.gui_click_element('#sign-in-form > div.relative.flex.items-center.justify-between.w-full.h-fit.mt-4 > div.relative.w-full > button:contains("Sign in")')

#     sb.sleep(2)

#     sb.save_screenshot("after login.png", "screenshots")

#     sb.click('button:contains("Continue")', 20)

#     sb.sleep(3)

#     sb.gui_click_element('div[class="checkbox-hitarea overlay -inset-1.5"]')

#     sb.click('button:contains("Next")')

#     sb.sleep(2)

#     sb.click('button:contains("Personal use")')

#     sb.sleep(2)

#     sb.click('button:contains("Text to speech")')

#     sb.sleep(1)

#     sb.click('button:contains("Continue")')

#     sb.sleep(1)

#     sb.click('button:contains("Skip")')

#     sb.sleep(3)

#     sb.open("https://elevenlabs.io/app/developers/api-keys")

#     sb.sleep(2)

#     sb.click('button:contains("Create Key")', 20)

#     sb.click('button[id*="restrict-key-toggle-_r_"]')
#     sb.sleep(0.4)

#     sb.click('[class="flex flex-col-reverse sm:flex-row sm:justify-end sm:space-x-2 border-t border-border p-4 -m-6 mt-0 gap-2"] button:nth-of-type(2)')

#     element = sb.find_element('input[data-agent-id*="input-_r_"][readonly=""][type="text"]')
#     attribute_value = element.get_attribute('value')
#     print(f"value attribute: {attribute_value}")
# finally:
#     sb.driver.stop()

