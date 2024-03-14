from selenium import webdriver
import time
import json
options = webdriver.ChromeOptions()
# options.add_argument(r"--user-data-dir=C:\\Users\\rohit\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
driver = webdriver.Chrome(options=options)
driver.get("https://web.snapchat.com/")
def save_cookie(driver, path):
    with open(path, 'w') as filehandler:
        json.dump(driver.get_cookies(), filehandler)
input("Press Enter to continue...")
save_cookie(driver, "cookies.json")
driver.quit()