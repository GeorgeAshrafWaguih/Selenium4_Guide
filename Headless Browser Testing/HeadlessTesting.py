from selenium import webdriver


def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("/chromedriver")
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(service=serv_obj, options= options)
    return driver


def headless_edge():
    from selenium.webdriver.edge.service import Service
    serv_obj = Service("/Users/georgeashraf/My-Github/Test_Automation_Framework_Python_Selenium/msedgedriver")
    options = webdriver.EdgeOptions()
    options.headless = True
    driver = webdriver.Edge(service=serv_obj, options= options)
    return driver


def headless_firefox():
    from selenium.webdriver.firefox.service import Service
    serv_obj = Service("/Users/georgeashraf/My-Github/Test_Automation_Framework_Python_Selenium/geckodriver")
    options = webdriver.FirefoxOptions()
    options.headless = True
    driver = webdriver.Firefox(service=serv_obj, options= options)
    return driver


driver = headless_chrome()  # For headless chrome testing
# driver = headless_edge()  # For headless edge testing
# driver = headless_firefox()  # For headless firefox testing
driver.get("https://demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)
