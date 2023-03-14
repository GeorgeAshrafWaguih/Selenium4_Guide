import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait

# Application commands
serv_obj=Service("/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(4)
driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()

time.sleep(4)
driver.close()
time.sleep(4)