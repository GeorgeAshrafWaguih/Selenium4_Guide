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

driver.get("https://demo.nopcommerce.com/")
#driver.find_element(By.LINK_TEXT, "Digital downloads").click()
#driver.find_element(By.PARTIAL_LINK_TEXT, "Digital").click()


# Find total number of links on the webpage
# Links = driver.find_elements(By.TAG_NAME, 'a')
Links = driver.find_elements(By.XPATH, '//a')
print("Total number of links: ", len(Links))

# Print all links
for link in Links:
    print(link.text)
time.sleep(4)