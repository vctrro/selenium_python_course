import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    # driver = webdriver.Firefox()
    driver = webdriver.Chrome()

    driver.get(link)
    time.sleep(2)

    num1 = driver.find_element(By.ID, "num1").text
    num2 = driver.find_element(By.ID, "num2").text
    sum = str(int(num1) + int(num2))
    select = Select(driver.find_element(By.ID, "dropdown"))
    select.select_by_value(sum)

    button = driver.find_element(By.CLASS_NAME, "btn-default")
    button.click()

    time.sleep(15)
finally:
    driver.quit()
    