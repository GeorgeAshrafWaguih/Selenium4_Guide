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
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
# driver.implicitly_wait(5)

# Scroll till certain pixel no
# driver.execute_script("window.scrollBy(0,3000)", "")
# value = driver.execute_script("return window.pageYOffset;")
# print(f'Number of pixels moved: {value}')

# Scroll till element is visible
# egypt_flag = driver.find_element(By.XPATH, "//img[@alt='Flag of Egypt']")
# driver.execute_script("arguments[0].scrollIntoView();", egypt_flag)
# value = driver.execute_script("return window.pageYOffset;")
# print(f'Number of pixels moved: {value}')

# Scroll till the end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print(f'Number of pixels moved: {value}')
time.sleep(2)

# Scroll back up the page
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print(f'Number of pixels moved: {value}')
time.sleep(2)