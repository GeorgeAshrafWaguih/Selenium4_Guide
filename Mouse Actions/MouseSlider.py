import time
import requests
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service("/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.implicitly_wait(5)

min_slider = driver.find_element(By.XPATH, '//*[@id="slider-range"]/span[1]')
max_slider = driver.find_element(By.XPATH, '//*[@id="slider-range"]/span[2]')

# location of sliders
print(min_slider.location)  # {'x': 59, 'y': 250}
print(max_slider.location)  # {'x': 479, 'y': 250}

# Move sliders
act = ActionChains(driver)
act.drag_and_drop_by_offset(min_slider, 150, 0).perform()
act.drag_and_drop_by_offset(max_slider, -30, 0).perform()

# Location of sliders after moving
print(min_slider.location)  # {'x': 210, 'y': 250}
print(max_slider.location)  # {'x': 450, 'y': 250}

time.sleep(5)