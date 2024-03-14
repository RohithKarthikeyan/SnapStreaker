import time
import json
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_camera" : 1,
    "profile.default_content_setting_values.media_stream_mic" : 1
})
# options.add_experimental_option("prefs", {
#     "profile.default_content_setting_values.media_stream_mic" : 1
# })
driver = webdriver.Chrome(options=options)
driver.get('https://web.snapchat.com/')
# time.sleep(20)
# driver.switch_to.window(driver.window_handles[0])
# time.sleep(30)
wait = WebDriverWait(driver, 1000)
login = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/div[3]/div[1]/div/button[1]")))
login.click()
driver.implicitly_wait(1)
driver.switch_to.window(driver.window_handles[1])
login = driver.find_element(By.ID, "accountIdentifier")
# wait = WebDriverWait(driver, timeout=2)
# wait.until(lambda d : login.is_displayed())
login.send_keys("rohithk01")
time.sleep(1)
login = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="account_identifier_form"]/div[3]/button')))
login.click()

login = driver.find_element(By.ID, "password")
login.send_keys("Rohith2005")
time.sleep(1)
login = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password_form"]/div[3]/button')))
login.click()
login = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div[4]/div[2]/button[1]')))
login.click()
login = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[3]/div/div/div/div[2]/div[1]/div/div/div/div/div/button')))
login.click()
time.sleep(0.5)
config_camera_url = "chrome://settings/content/camera"
driver.get(config_camera_url)
time.sleep(3)  # Wait until selector appears
selector = driver.execute_script(
    "return document.querySelector('settings-ui')"
    ".shadowRoot.querySelector('settings-main')"
    ".shadowRoot.querySelector('settings-basic-page')"
    ".shadowRoot.querySelector('settings-section > settings-privacy-page')"
    ".shadowRoot.querySelector('settings-animated-pages > settings-subpage > media-picker')"
    ".shadowRoot.querySelector('#picker > #mediaPicker')"
    ".value = 'OBS Virtual Camera'"  # Change for your default camera
)
login = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="downshift-160-toggle-button"]')))
login.click()
time.sleep(0.5)
login = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="downshift-189-item-1"]')))
login.click()
# //*[@id="downshift-941-item-1"]
# //*[@id="downshift-1013-toggle-button"]

# login = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[3]/div/div/div/div[2]/div[1]/div/div/div/div/div/button/svg[1]')))
# login.click()
# login = driver.find_element(By.XPATH, '//*[@id="account_identifier_form"]/div[3]/button')
input("Press Enter to continue...")
driver.quit()