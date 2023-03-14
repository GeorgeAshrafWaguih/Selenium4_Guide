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
driver.get("https://text-compare.com/")

# Capture textbox 1 & 2
input1 = driver.find_element(By.XPATH, "//textarea[@id='inputText1']")
input2 = driver.find_element(By.XPATH, "//textarea[@id='inputText2']")

# Enter value in textbox 1
input1.send_keys("Welcome to this test!")

act = ActionChains(driver)

# Cmd+A (Select all text)

# act.key_down(Keys.COMMAND)
# act.send_keys("a")
# act.key_up(Keys.COMMAND)
# act.perform()

# Can be added in one single line of code
act.key_down(Keys.COMMAND).send_keys("a").key_up(Keys.COMMAND).perform()

# Cmd+C (Copy selected text)
act.key_down(Keys.COMMAND).send_keys("c").key_up(Keys.COMMAND).perform()

# Tab (Move to input text 2)
act.send_keys(Keys.TAB).perform()

# Cmd+v (Paste selected text)
act.key_down(Keys.COMMAND).send_keys("v").key_up(Keys.COMMAND).perform()

print(input2.text)
time.sleep(3)