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

# Username and password are added in syntax username:password@url
# Syntax :  http://username:password@url.com
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

print(driver.find_element(By.XPATH, '//*[@id="content"]/div/p').text)
