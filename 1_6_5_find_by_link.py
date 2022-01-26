import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_link_text"

try:
    # driver = webdriver.Firefox()
    driver = webdriver.Chrome()

    driver.get(link)
    time.sleep(1)

    link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))

    driver.find_element(By.LINK_TEXT, link_text).click()
    time.sleep(1)

    driver.find_element(By.XPATH, "//input[@name='first_name']").send_keys("Vc")
    driver.find_element(By.XPATH, "//input[@name='last_name']").send_keys("Ro")
    driver.find_element(By.XPATH, "//input[@name='firstname']").send_keys("Mo")
    driver.find_element(By.XPATH, "//input[@id='country']").send_keys("Ro")

    driver.find_element(By.CLASS_NAME, "btn").click()

    time.sleep(15)
finally:
    driver.quit()
    