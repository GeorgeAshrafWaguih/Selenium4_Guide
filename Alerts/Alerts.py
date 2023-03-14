import time
import requests
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj=Service("/chromedriver")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(2)

alert_window = driver.switch_to.alert
print(alert_window.text)
msg = "welcome"
alert_window.send_keys(msg)
time.sleep(2)
alert_window.accept()  # close alert window by using Ok
#alert_window.dismiss()  # close alert window by using Cancel
time.sleep(2)


exp_msg = f'You entered: {msg}'
act_msg = driver.find_element(By.ID, "result").text
if exp_msg == act_msg:
    print("Test Passed")
