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

# Capture cookies from browser
cookies = driver.get_cookies()
print(f'No of cookies: {len(cookies)}')

# Print details of all cookies
for cookie in cookies:
    print(f'Name: {cookie.get("name")} , Value: {cookie.get("value")} , Expiry: {cookie.get("expiry")}')

# Add new cookie to browser
driver.add_cookie({"name": "MyCookie", "value": "123456"})
cookies = driver.get_cookies()   # Detect again the cookies after adding the new cookie
print(f'No of cookies: {len(cookies)}')

# Delete specific cookie from browser
driver.delete_cookie("MyCookie")
cookies = driver.get_cookies()   # Detect again the cookies after deleting the new cookie
print(f'No of cookies: {len(cookies)}')

# Delete all cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()   # Detect again the cookies after deleting all the cookies
print(f'No of cookies: {len(cookies)}')