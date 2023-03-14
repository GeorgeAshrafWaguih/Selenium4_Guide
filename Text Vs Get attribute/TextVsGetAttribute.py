import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://admin-demo.nopcommerce.com/login/")
email = driver.find_element(By.XPATH, '//*[@id="Email"]')
print("Get attribute:"+email.get_attribute('value'))
email.clear()
email.send_keys("Geo")
print(email.get_attribute('value'))
print("Get Text:"+email.text)
print(driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button').text)
driver.quit()