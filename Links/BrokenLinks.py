import time

import requests
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj=Service("/chromedriver")
driver = webdriver.Chrome(service=serv_obj)

driver.get("http://www.deadlinkcity.com/")

allLinks = driver.find_elements(By.TAG_NAME, 'a')
count = 0

for link in allLinks:
    url = link.get_attribute('href')
    try:
        response = requests.head(url)
    except:
        None

    if response.status_code >= 400:
        print(f'{url} is broken ')
        count += 1
    else:
        print(f'{url} is valid link')

print(f'Total number of broken links: {count}')