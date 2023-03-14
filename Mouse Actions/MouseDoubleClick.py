import time
import requests
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service("/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.implicitly_wait(5)

driver.switch_to.frame("iframeResult")  # Switch to the frame

field1 = driver.find_element(By.XPATH, '//*[@id="field1"]')
field1.clear()
field1.send_keys("Welcome this is a test!")

copy_text_button = driver.find_element(By.XPATH, "//button[normalize-space()='Copy Text']")

# Double Click Action
act = ActionChains(driver)
act.double_click(copy_text_button).perform()

field2 = driver.find_element(By.XPATH, '//*[@id="field2"]')
print(f'field 2: {field2.text}')
time.sleep(3)