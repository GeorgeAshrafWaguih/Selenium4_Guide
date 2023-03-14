import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
location = os.getcwd()


def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("/chromedriver")

    # Setting the download location to be your current folder
    prefences = {"download.default_directory": location}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", prefences)

    driver = webdriver.Chrome(service=serv_obj, options=ops)
    return driver


def edge_setup():
    from selenium.webdriver.edge.service import Service
    serv_obj = Service("/Users/georgeashraf/My-Github/Test_Automation_Framework_Python_Selenium/msedgedriver")

    # Setting the download location to be your current folder
    prefences = {"download.default_directory": location}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", prefences)

    driver = webdriver.Edge(service=serv_obj, options=ops)
    return driver


def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    serv_obj = Service("/Users/georgeashraf/My-Github/Test_Automation_Framework_Python_Selenium/geckodriver")

    # settings
    options = webdriver.FirefoxOptions()
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/msword")
    options.set_preference("browser.download.manager.showWhenStarting", False)
    options.set_preference("browser.download.folderList", 2)  # 0 desktop, 1 default location, 2 desired location
    options.set_preference("browser.download.dir", location)

    driver = webdriver.Firefox(service=serv_obj, options=options)
    return driver


# Run code
driver = chrome_setup()  # For Chrome browser
# driver = edge_setup()  # For Edge browser
# driver = firefox_setup()  # For Firefox browser
driver.implicitly_wait(5)
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
button = driver.find_element(By.XPATH, '//*[@id="table-files"]/tbody/tr[1]/td[5]/a')
driver.execute_script("arguments[0].click();", button)
driver.back()
driver.execute_script("arguments[0].click();", button)
time.sleep(5)
