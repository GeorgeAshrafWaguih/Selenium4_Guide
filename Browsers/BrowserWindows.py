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
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(5)
windowID = driver.current_window_handle
#print(windowID)

driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
windowIDs = driver.window_handles

# Approach 1 to capture window IDs
# parentWindow = windowIDs[0]
# childWindow = windowIDs[1]

# driver.switch_to.window(childWindow)
# print(f'Child window title: {driver.title}')
#
# driver.switch_to.window(parentWindow)
# print(f'Parent window title: {driver.title}')


# 2nd approach for capturing window IDS
# for ID in windowIDs:
#     driver.switch_to.window(ID)
#     print(driver.title)

# Close specific window
for ID in windowIDs:
    driver.switch_to.window(ID)
    if driver.title == "OrangeHRM":
        driver.close()

time.sleep(3)