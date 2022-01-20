import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/huge_form.html"

try:
    # driver = webdriver.Firefox()
    driver = webdriver.Chrome()

    driver.get(link)
    time.sleep(1)

    list = driver.find_elements(By.XPATH, "//div[@class='first_block']//input")

    for item in list:
        item.send_keys("Vc")

    driver.find_element(By.CLASS_NAME, "btn").click()

    time.sleep(15)
finally:
    driver.quit()
    