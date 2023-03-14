import time
import requests
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

serv_obj = Service("/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com/")

# register_link = Keys.COMMAND+Keys.RETURN
# driver.find_element(By.LINK_TEXT, "Register").send_keys(register_link)

# Selenium 4 : open new tab
# driver.get("https://www.opencart.com/")
# driver.switch_to.new_window('tab')
# driver.get("https://www.google.com/")

# Selenium 4 : Open new browser window
driver.get("https://www.opencart.com/")
driver.switch_to.new_window('window')
driver.get("https://www.google.com/")

time.sleep(4)
