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

driver.get("https://mypage.rediff.com/login/dologin")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)