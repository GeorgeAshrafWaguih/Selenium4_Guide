from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import mysql.connector

serv_obj = Service("/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
driver.implicitly_wait(10)

driver.find_element(By.XPATH, '//*[@id="wzrk-cancel"]').click()  # close welcome banner
try:
    # Get the data from db
    connection = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="root", database="mydb")
    cursor = connection.cursor()  # create a cursor
    cursor.execute("select * from caldata")  # execute query
    for row in cursor:
        # Getting all data from db
        principle_amount = row[0]
        rate = row[1]
        period1 = row[2]
        period2 = row[3]
        frequency = row[4]
        expected_maturity_value = row[5]

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
            print('test passed')
        else:
            print('test failed')

        driver.find_element(By.XPATH, '//*[@id="fdMatVal"]/div[2]/a[2]/img').click()  # Clear fields for the next iteration
    connection.close()  # Close connection to db
except:
    print("Connection unsuccessful")
