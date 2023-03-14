import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait

serv_obj=Service("/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.google.com")

driver.implicitly_wait(5)  # Implicit wait
driver.find_element(By.XPATH, '//*[@id="SIvCob"]/a').click()
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium")
search_box.submit()

driver.find_element(By.XPATH, "//h3[text()='Selenium']").click()
time.sleep(4)
driver.quit()
