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

driver.save_screenshot(os.getcwd() + "/homepage.png")
driver.get_screenshot_as_file(os.getcwd() + "/homepage1.png")

# Both of the below methods saves the screenshot in a Binary format
# driver.get_screenshot_as_png()
# driver.get_screenshot_as_base64()
