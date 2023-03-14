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
driver.get("https://jqueryui.com/datepicker/")
driver.implicitly_wait(5)

driver.switch_to.frame(0)  # switch to frame

# format for date field mm/dd/yyyy
# driver.find_element(By.ID, "datepicker").send_keys("03/30/2023")

# Compare date when clicking on date field and keep going to the next month till reached specific month
expected_year = "2024"
expected_month = "March"
expected_date = "29"

driver.find_element(By.ID, "datepicker").click()

while True:
    displayed_month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    displayed_year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if displayed_month == expected_month and displayed_year == expected_year:
        break
    else:
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()  # next arrow
        # driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']").click()  # previous arrow

dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for date in dates:
    if date.text == expected_date:
        date.click()
        break


# driver.find_element(By.XPATH, "//a[@data-date='29']").click()
# //a[@data-date='29']

time.sleep(3)

