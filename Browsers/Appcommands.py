from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Application commands
serv_obj=Service("/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://opensource-demo.orangehrmlive.com/")

print(driver.title)
print(driver.current_url)
# print(driver.page_source)

