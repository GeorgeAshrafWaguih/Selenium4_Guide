# 1) count number of rows & columns
# 2) Read specific row & column Data
# 3) Read all the rows & columns Data
# 4) Read data based on condition (List books name whose author is Mukesh)

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
driver.get("https://testautomationpractice.blogspot.com/")

# 1) count number of rows & columns
noOfRows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))
# Length of trs in Xpath represents rows
noOfColumns = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr[1]/th"))
# No of th represents no of columns
print(f'Rows: {noOfRows} , Columns:{noOfColumns}')

# 2) Read specific row & column Data
print(driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[1]").text)
#  Get the value in the 5th row and 1st column -- Master In Selenium

# 3) Read all the rows & columns Data
print("All rows and colums ")
for r in range(2, noOfRows+1):
    for c in range(1, noOfColumns+1):
        data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(data, end="          ")
    print()

# 4) Read data based on condition (List books name whose author is Mukesh)
for r in range(2, noOfRows+1):
    author = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[2]").text
    if author == 'Mukesh':
        bookname = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[1]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]").text
        print(f'{bookname}    {author}    {price}')
