import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com/register/")
driver.get("https://www.google.com/")
time.sleep(4)
driver.refresh()
time.sleep(4)
driver.back()
time.sleep(4)
driver.forward()
time.sleep(4)