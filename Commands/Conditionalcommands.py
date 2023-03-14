from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com/register/")

print(driver.find_element(By.XPATH, "//input[@id='small-searchterms']").is_displayed())
print(driver.find_element(By.XPATH, "//input[@id='small-searchterms']").is_enabled())

print(driver.find_element(By.XPATH, "//input[@id='gender-male']").is_selected())
driver.find_element(By.XPATH, "//input[@id='gender-male']").click()
print(driver.find_element(By.XPATH, "//input[@id='gender-male']").is_selected())

driver.quit()