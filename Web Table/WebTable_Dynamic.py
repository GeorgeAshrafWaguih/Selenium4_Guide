import time
import requests
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
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
driver.find_element(By.XPATH, "//span[normalize-space()='Admin']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='User Management']").click()
driver.find_element(By.XPATH, "//a[normalize-space()='Users']").click()

# Total rows in the table
noOfRows = len(driver.find_elements(By.XPATH, "//div[@class='oxd-table-body']/div"))
print(noOfRows)

# Counting the Enabled and Disabled users
noOfEnabledUsers = 0
noOfDisabledUsers = 0
for r in range(2, noOfRows+1):
    userStatus = driver.find_element(By.XPATH, "//div[@class='oxd-table-body']/div["+str(r)+"]/div/div[5]").text
    if userStatus == 'Enabled':
        noOfEnabledUsers += 1
    elif userStatus == 'Disabled':
        noOfDisabledUsers += 1

print(f'No of Enabled users: {noOfEnabledUsers}')
print(f'No of Disabled users: {noOfDisabledUsers}')


# Print from the table Username and UserRoles only if UserRole is 'ESS'
ESS_usercount = 0
Admin_usercount = 0
for r in range(2, noOfRows+1):
    userRole = driver.find_element(By.XPATH, "//div[@class='oxd-table-body']/div["+str(r)+"]/div/div[3]").text
    if userRole == 'ESS':
        username = driver.find_element(By.XPATH, "//div[@class='oxd-table-body']/div["+str(r)+"]/div/div[2]").text
        ESS_usercount += 1
        print(f'{username} : {userRole}')
    elif userRole == 'Admin':
        Admin_usercount += 1
print(f'No of ESS users: {ESS_usercount}')
print(f'No of Admin users: {Admin_usercount}')
print(f'Total number of users: {noOfRows-1}')

