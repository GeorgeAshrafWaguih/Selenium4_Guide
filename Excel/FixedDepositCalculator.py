import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import XLUtils

serv_obj = Service("/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
driver.implicitly_wait(10)

driver.find_element(By.XPATH, '//*[@id="wzrk-cancel"]').click()  # close welcome banner

file = '/caldata.xlsx'
rows = XLUtils.getRowCount(file, "Sheet1")

for r in range(2, rows+1):  # We will skip the 1st row because it is all titles and not values in excell sheet
    principle_amount = XLUtils.readData(file, "Sheet1", r, 1)
    rate = XLUtils.readData(file, "Sheet1", r, 2)
    period1 = XLUtils.readData(file, "Sheet1", r, 3)
    period2 = XLUtils.readData(file, "Sheet1", r, 4)
    frequency = XLUtils.readData(file, "Sheet1", r, 5)
    expected_maturity_value = XLUtils.readData(file, "Sheet1", r, 6)

    # passing data to application
    driver.find_element(By.XPATH, '//*[@id="principal"]').send_keys(principle_amount)
    driver.find_element(By.XPATH, '//*[@id="interest"]').send_keys(rate)
    driver.find_element(By.XPATH, '//*[@id="tenure"]').send_keys(period1)

    period_dropdown = Select(driver.find_element(By.XPATH, '//*[@id="tenurePeriod"]'))
    period_dropdown.select_by_visible_text(period2)

    frequency_dropdown = Select(driver.find_element(By.XPATH, '//*[@id="frequency"]'))
    frequency_dropdown.select_by_visible_text(frequency)

    driver.find_element(By.XPATH, '//*[@id="fdMatVal"]/div[2]/a[1]/img').click()

    actual_maturity_value = driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text

    # Validation
    if float(expected_maturity_value) == float(actual_maturity_value):
        print(f'{r} test passed')
        XLUtils.writeData(file, "Sheet1", r, 8, "Passed")  # write the status in the sheet
        XLUtils.fillGreenColor(file, "Sheet1", r, 8)  # fill the color in the cell

    else:
        print(f'{r} test failed')
        XLUtils.writeData(file, "Sheet1", r, 8, "Failed")  # write the status in the sheet
        XLUtils.fillRedColor(file, "Sheet1", r, 8)  # fill the color in the cell

    driver.find_element(By.XPATH, '//*[@id="fdMatVal"]/div[2]/a[2]/img').click()  # Clear fields for the next iteration


