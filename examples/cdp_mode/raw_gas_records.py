"""(Bypasses the Imperva/Incapsula hCaptcha)"""
from seleniumbase import SB

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

url = "https://elevenlabs.io/app/sign-up"

w=random.randint(9999, 12000)

print(w)


with SB(uc=True) as sb:
    sb.activate_cdp_mode(url)
    sb.sleep(4)

    sb.cdp.press_keys('input[name="email"]', f"ytprojectelevenlabsacckbkb{9990+w}@catchmail.io")  # human-speed
    sb.cdp.press_keys('input[name="password"]', "Prince!4438#")

    # Standard syntax for clicking a button containing specific text in  Mode
    sb.cdp.click('div[data-testid="signup-signup-button-div"] button:contains("Sign up")')

    sb.cdp.sleep(0.2)

    sb.cdp.solve_captcha()

    sb.cdp.sleep(2)

    sb.cdp.save_screenshot("after sign up.png", "screenshots")

    sb.cdp.sleep(4)

    sb.cdp.save_screenshot("after sign up after 2.png", "screenshots")

    link=generate_vlink(9990+w)

    sb.cdp.open(link)

    sb.cdp.sleep(5)

    sb.cdp.click('button:contains("Continue")')

    sb.cdp.sleep(1)

    sb.cdp.press_keys('input[name="password"]', "Prince!4438#")

    sb.cdp.save_screenshot("before sign in.png", "screenshots")

    sb.cdp.sleep(1)

    # Standard syntax for clicking a button containing specific text in  Mode
    sb.cdp.gui_click_element('#sign-in-form > div.relative.flex.items-center.justify-between.w-full.h-fit.mt-4 > div.relative.w-full > button:contains("Sign in")')

    sb.cdp.sleep(2)

    sb.cdp.save_screenshot("after login.png", "screenshots")

    sb.cdp.click('button:contains("Continue")', 20)

    sb.cdp.sleep(3)

    sb.cdp.gui_click_element('div[class="checkbox-hitarea overlay -inset-1.5"]')

    sb.cdp.click('button:contains("Next")')

    sb.cdp.sleep(2)

    sb.cdp.click('button:contains("Personal use")')

    sb.cdp.sleep(2)

    sb.cdp.click('button:contains("Text to speech")')

    sb.cdp.sleep(1)

    sb.cdp.click('button:contains("Continue")')

    sb.cdp.sleep(1)

    sb.cdp.click('button:contains("Skip")')

    sb.cdp.sleep(3)

    sb.cdp.open("https://elevenlabs.io/app/developers/api-keys")

    sb.cdp.sleep(2)

    sb.cdp.click('button:contains("Create Key")', 20)

    sb.cdp.click('button[id*="restrict-key-toggle-_r_"]')
    sb.cdp.sleep(0.4)

    sb.cdp.click('[class="flex flex-col-reverse sm:flex-row sm:justify-end sm:space-x-2 border-t border-border p-4 -m-6 mt-0 gap-2"] button:nth-of-type(2)')

    element = sb.cdp.find_element('input[data-agent-id*="input-_r_"][readonly=""][type="text"]')
    attribute_value = element.get_attribute('value')
    print(f"value attribute: {attribute_value}")
