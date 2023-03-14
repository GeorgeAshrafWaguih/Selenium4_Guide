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
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(5)

# Login
driver.find_element(By.NAME, "username").send_keys("admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Navigate to users
# admin = driver.find_element(By.XPATH, "//span[normalize-space()='Admin']")
# user_management = driver.find_element(By.XPATH, "//span[normalize-space()='User Management']")
# users = driver.find_element(By.XPATH, "//a[normalize-space()='Users']")

# Mouse Hover and click action
act = ActionChains(driver)
admin = driver.find_element(By.XPATH, "//span[normalize-space()='Admin']")
act.move_to_element(admin).click().perform()
user_management = driver.find_element(By.XPATH, "//span[normalize-space()='User Management']")
act.move_to_element(user_management).click().perform()
users = driver.find_element(By.XPATH, "//a[normalize-space()='Users']")
act.move_to_element(users).perform()


time.sleep(3)



