import time
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj=Service("/chromedriver")
driver = webdriver.Chrome(service=serv_obj)

my_wait = WebDriverWait(driver, 10, ignored_exceptions=[NoSuchElementException,
                                                        ElementNotVisibleException,
                                                        ElementNotSelectableException,
                                                        Exception])   # Explicit wait declaration


driver.get("https://www.google.com")

driver.find_element(By.XPATH, '//*[@id="SIvCob"]/a').click()
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium")
search_box.submit()

search_result = my_wait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']")))
search_result.click()


time.sleep(4)
driver.quit()
