import time
import requests
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service("/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container']").click()


countries_list = driver.find_elements(By.XPATH, "//ul[@id='select2-billing_country-results']/li")
print(len(countries_list))
for country in countries_list:
    if country.text == 'Georgia':
        country.click()
        break
time.sleep(2)