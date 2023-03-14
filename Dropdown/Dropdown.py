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

driver.get("https://www.opencart.com/index.php?route=account/register")

# dropdowm_country_element = driver.find_element(By.NAME, 'country_id')
country = Select(driver.find_element(By.NAME, 'country_id'))

# Select dropdown option
country.select_by_visible_text("Bahamas")  # Bahamas
# time.sleep(3)
country.select_by_value('10')  # Argentine
# time.sleep(3)
country.select_by_index(20)  # Belarus
# time.sleep(3)

# Capture all the options and print them
all_countries = country.options
print(f'Total number of countries: {len(all_countries)}')

for option in all_countries:
    print(option.text)

# Select option from dropdown without using built-in methods
for option in all_countries:
    if option.text == "Aruba":
        option.click()
        break
# time.sleep(3)

# allOptions = driver.find_elements(By.XPATH, '//*[@name="country_id"/option]')
# print(len(allOptions))


