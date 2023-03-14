from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(5)
driver.find_element(By.NAME, "username").send_keys("admin")  # username field
driver.find_element(By.NAME, "password").send_keys("admin123")  # password field
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()  # login button
expected_title = "OrangeHRM"
actual_title = driver.title

if actual_title == expected_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

driver.close()
