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
driver.get("https://fineuploader.com/demos.html")
driver.implicitly_wait(5)
driver.find_element(By.XPATH, '//*[@id="fine-uploader-gallery"]/div/div[3]/input').click()
driver.find_element(By.XPATH, '//*[@id="trigger-upload"]').send_keys("/Users/georgeashraf/My-Github/Test_Automation_Framework_Python_Selenium/file-sample_150kB.pdf")

time.sleep(5)