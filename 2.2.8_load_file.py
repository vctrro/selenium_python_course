import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/file_input.html"

try:
    # driver = webdriver.Firefox()
    driver = webdriver.Chrome()

    driver.get(link)
    time.sleep(1)

    current_dir = os.path.abspath(os.path.abspath(os.path.dirname(__file__)))
    file = os.path.join(current_dir, "file.txt")

    driver.find_element(By.NAME, "firstname").send_keys("Vc")
    driver.find_element(By.NAME, "lastname").send_keys("Ro")
    driver.find_element(By.NAME, "email").send_keys("vc@ro.us")

    driver.find_element(By.NAME, "file").send_keys(file)

    button = driver.find_element(By.CLASS_NAME, "btn-primary")
    button.click()

    time.sleep(15)
finally:
    driver.quit()
    