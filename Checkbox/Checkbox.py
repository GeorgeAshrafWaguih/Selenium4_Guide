import time
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj=Service("/chromedriver")
driver = webdriver.Chrome(service=serv_obj)

# my_wait = WebDriverWait(driver, 10, ignored_exceptions=[NoSuchElementException,
#                                                         ElementNotVisibleException,
#                                                         ElementNotSelectableException,
#                                                         Exception])   # Explicit wait declaration


driver.get("https://itera-qa.azurewebsites.net/home/automation")

#driver.find_element(By.XPATH,'//*[@id="monday"]').click()

# Selecting multiple checkboxes
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes))

# way 1:
# for i in range(len(checkboxes)):
#     checkboxes[i].click()

# way 2:
# for checkbox in checkboxes:
#     checkbox.click()

# way 3: Select multiple checkboxes based on choice
# for checkbox in checkboxes:
#     weekname = checkbox.get_attribute('id')
#     if weekname=="monday" or weekname=="sunday":
#         checkbox.click()

# way 4 : select last 2 checkboxes
# for i in range(len(checkboxes)-2,len(checkboxes)):
#     checkboxes[i].click()

# way 5: select first 2 checkboxes
for i in range(len(checkboxes)):
    if i < 2:
        checkboxes[i].click()

# way 6: clear all checkboxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()

time.sleep(3)